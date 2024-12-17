from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [[num] for num in nums]
        max_len, max_idx = 0, 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
            if len(dp[i]) > max_len:
                max_len = len(dp[i])
                max_idx = i

        return dp[max_idx]