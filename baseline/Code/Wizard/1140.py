from typing import List
class Solution:
    def stoneGame(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

        for diff in range(1, n):
            for i in range(n - diff):
                j = i + diff
                for x in range(1, diff + 1):
                    dp[i][j] = max(dp[i][j], min(dp[i + x][j], piles[i] + dp[i + x][j - 1]))

        return dp[0][n - 1]