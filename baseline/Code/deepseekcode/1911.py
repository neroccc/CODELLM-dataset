from typing import List
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        even, odd = nums[0], 0
        for i in range(1, n):
            even, odd = max(even, odd + nums[i]), max(odd, even - nums[i])
        return max(even, odd)