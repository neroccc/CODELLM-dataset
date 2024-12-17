from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        dp_max = [nums[0]] * n
        dp_min = [nums[0]] * n

        for i in range(1, n):
            if nums[i] > 0:
                dp_max[i] = max(nums[i], dp_max[i - 1] * nums[i])
                dp_min[i] = min(nums[i], dp_min[i - 1] * nums[i])
            else:
                dp_max[i] = max(nums[i], dp_min[i - 1] * nums[i])
                dp_min[i] = min(nums[i], dp_max[i - 1] * nums[i])

            ans = max(ans, dp_max[i])

        return ans