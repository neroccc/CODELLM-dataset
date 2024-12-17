from typing import List
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        for _ in range(maxMove):
            new_dp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i > 0:
                        new_dp[i - 1][j] += dp[i][j]
                    if i < m - 1:
                        new_dp[i + 1][j] += dp[i][j]
                    if j > 0:
                        new_dp[i][j - 1] += dp[i][j]
                    if j < n - 1:
                        new_dp[i][j + 1] += dp[i][j]
            dp = new_dp
        return sum(map(sum, dp)) % mod
