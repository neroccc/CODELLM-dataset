from typing import List
class Solution:
    def stoneGame(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = stones[i]
            for j in range(i + 1, n):
                dp[i][j] = max(stones[i] - dp[i + 1][j], stones[j] - dp[i][j - 1])

        return dp[0][n - 1]