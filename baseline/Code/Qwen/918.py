from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        cur_max = 0
        cur_min = 0

        for i in range(n):
            total += nums[i]
            cur_max = max(cur_max + nums[i], nums[i])
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min + nums[i], nums[i])
            min_sum = min(min_sum, cur_min)

        if max_sum > 0:
            return max(max_sum, total - min_sum)
        else:
            return max_sum