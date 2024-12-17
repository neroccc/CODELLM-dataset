from typing import List
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix_sum = [0] * n
        prefix_sum[0] = stones[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + stones[i]

        dp = [0] * n
        dp[-1] = prefix_sum[-1]
        for i in range(n - 2, -1, -1):
            dp[i] = max(prefix_sum[i] - dp[i + 1], dp[i + 1])

        return dp[0]