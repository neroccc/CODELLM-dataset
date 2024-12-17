from typing import List
class Solution:
    def maxCompatibility(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        n = len(students)
        dp = [[0] * (1 << n) for _ in range(n + 1)]
        score = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                for k in range(len(students[i])):
                    if students[i][k] == mentors[j][k]:
                        score[i][j] += 1

        for i in range(n):
            dp[1][1 << i] = score[0][i]

        for i in range(2, n + 1):
            for j in range(1 << n):
                if bin(j).count('1') == i:
                    for k in range(n):
                        if ((j >> k) & 1) == 1:
                            dp[i][j] = max(dp[i][j], dp[i - 1][j ^ (1 << k)] + score[i - 1][k])

        return dp[n][(1 << n) - 1]