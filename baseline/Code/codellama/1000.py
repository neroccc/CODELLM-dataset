from typing import List
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [0] * (sum(stones) + 1)
        for i in range(n):
            for j in range(stones[i], sum(stones) + 1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return sum(stones) - 2 * dp[-1]