from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        count = 0

        for i in range(n - 2):
            d = nums[i + 1] - nums[i]
            dp[i] = 1
            for j in range(i + 2, n):
                if nums[j] - nums[j - 1] == d:
                    dp[j] = dp[j - 1] + 1
                else:
                    d = nums[j] - nums[j - 1]
                    dp[j] = 1
                count += dp[j]

        return count