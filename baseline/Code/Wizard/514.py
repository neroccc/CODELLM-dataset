from typing import List
class Solution:
    def minSteps(self, ring: str, key: str) -> int:
        n, m = len(ring), len(key)
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if ring[i] == key[j]:
                    dp[i][j] = 0 if i == 0 or j == 0 else dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[-1][-1]