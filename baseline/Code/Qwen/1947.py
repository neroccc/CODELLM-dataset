from typing import List
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        n = len(students)
        m = len(students[0])
        students_scores = [[0] * n for _ in range(n)]
        mentors_scores = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                for k in range(m):
                    if students[i][k] == mentors[j][k]:
                        students_scores[i][j] += 1
                        mentors_scores[j][i] += 1

        dp = [[0] * (1 << n) for _ in range(n + 1)]

        for i in range(n):
            for j in range(1 << n):
                if j & (1 << i) == 0:
                    continue
                for k in range(n):
                    if j & (1 << k) == 0:
                        continue
                    dp[i + 1][j | (1 << k)] = max(
                        dp[i + 1][j | (1 << k)],
                        dp[i][j] + students_scores[i][k] + mentors_scores[k][i],
                    )

        return dp[n][(1 << n) - 1]