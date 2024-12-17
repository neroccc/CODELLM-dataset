from typing import List
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * 10001
        for num in nums:
            dp[num] += num
        for i in range(1, 10001):
            dp[i] = max(dp[i - 1], dp[i] + dp[i - 2])
        return dp[-1]