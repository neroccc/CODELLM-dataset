from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        dp = [0] * n
        diff = nums[1] - nums[0]
        count = 0

        for i in range(2, n):
            if nums[i] - nums[i - 1] == diff:
                dp[i] = dp[i - 1] + 1
                count += dp[i]
            else:
                diff = nums[i] - nums[i - 1]

        return count