from typing import List
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        dp = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        for i in range(n):
            for j in range(n):
                if ring[i] == key[j]:
                    dp[i][j] = 0

        for diff in range(1, n):
            for i in range(n - diff):
                j = i + diff
                if ring[i] == key[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1

        return dp[0][-1] + n