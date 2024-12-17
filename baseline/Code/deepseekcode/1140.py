from typing import List
class Solution:
    def stoneGame(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        sum_piles = [0] * (n + 1)

        for i in range(n):
            sum_piles[i + 1] = sum_piles[i] + piles[i]

        for i in range(n - 1, -1, -1):
            dp[i][i] = piles[i]
            for j in range(i + 1, n):
                dp[i][j] = max(piles[i] + sum_piles[j + 1] - sum_piles[i + 1] - dp[i + 1][j],
                               piles[j] + sum_piles[j] - sum_piles[i] - dp[i][j - 1])

        return dp[0][n - 1]