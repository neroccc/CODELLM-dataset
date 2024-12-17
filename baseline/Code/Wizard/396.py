from typing import List
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        curr_sum = sum(nums)

        max_sum = 0
        for i in range(n):
            max_sum = max(max_sum, curr_sum)
            curr_sum -= n * nums[n - 1]
            n -= 1

        return max_sum