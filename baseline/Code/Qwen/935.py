from typing import List
class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * 10 for _ in range(n)]
        dp[0] = [1] * 10

        for i in range(1, n):
            for j in range(10):
                for k in [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]:
                    x, y = j + k[0], j + k[1]
                    if 0 <= x < 10 and 0 <= y < 10:
                        dp[i][j] += dp[i - 1][x]
                        dp[i][j] %= MOD

        return sum(dp[-1]) % MOD