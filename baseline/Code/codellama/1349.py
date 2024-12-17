from typing import List
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if seats[i][j] == '.':
                    dp[i][j] = 1
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]
                    if i < m - 1:
                        dp[i][j] += dp[i + 1][j]
                    if j < n - 1:
                        dp[i][j] += dp[i][j + 1]
        return max(max(row) for row in dp)
