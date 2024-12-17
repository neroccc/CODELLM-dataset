from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')
        min_sum = float('inf')
        total = 0
        current_sum = 0

        for num in nums:
            total += num
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)
            min_sum = min(min_sum, current_sum)

        max_sum_not_circular = total - min_sum

        max_sum_circular = float('-inf')
        current_sum = 0

        for i in range(n):
            current_sum += nums[i]
            max_sum_circular = max(max_sum_circular, current_sum)

        return max(max_sum, max_sum_circular)