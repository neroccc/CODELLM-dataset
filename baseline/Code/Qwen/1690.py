from typing import List
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                diff = prefix[j + 1] - prefix[i + 1] - dp[i + 1][j]
                dp[i][j] = max(diff - stones[i], diff - stones[j])

        return dp[0][n - 1]