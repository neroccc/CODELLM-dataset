from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_len = 1
        for i in range(1, n):
            if nums[i] == 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 0
            max_len = max(max_len, dp[i])

        dp2 = [0] * n
        dp2[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            if nums[i] == 1:
                dp2[i] = dp2[i + 1] + 1
            else:
                dp2[i] = 0

        for i in range(n - 1):
            if dp[i] == 0 and dp2[i + 1] == 0:
                return max(max_len, 0)
            max_len = max(max_len, dp[i] + dp2[i + 1])

        return max_len