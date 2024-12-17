from typing import List
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        F = sum(i * num for i, num in enumerate(nums))
        total = sum(nums)
        max_F = F

        for i in range(n - 1, 0, -1):
            F += total - n * nums[i]
            max_F = max(max_F, F)

        return max_F