from typing import List
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (goal + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i][0] = 1
            for j in range(1, goal + 1):
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][max(0, j - k)]) % MOD
        return dp[n][goal]