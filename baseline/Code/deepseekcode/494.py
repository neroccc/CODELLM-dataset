from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if total_sum < abs(target) or (total_sum + target) % 2 == 1:
            return 0
        neg_target = (total_sum + target) // 2
        dp = [0] * (neg_target + 1)
        dp[0] = 1
        for num in nums:
            for i in range(neg_target, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[-1]