from typing import List
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1

        for _ in range(maxMove):
            new_dp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if 0 <= ni < m and 0 <= nj < n:
                            new_dp[ni][nj] += dp[i][j]
                            new_dp[ni][nj] %= MOD
                        else:
                            new_dp[i][j] += dp[i][j]
                            new_dp[i][j] %= MOD
            dp = new_dp

        return sum(map(sum, dp)) % MOD