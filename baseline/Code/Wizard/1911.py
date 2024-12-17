from typing import List
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        dp2 = [0] * n
        dp2[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            dp2[i] = max(dp2[i + 1] + nums[i], nums[i])

        ans = 0
        for i in range(n):
            ans = max(ans, dp[i] - dp2[i + 1])

        return ans