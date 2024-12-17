from typing import List
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_sum = float('-inf')
        for i in range(n - k):
            max_sum = max(max_sum, sum(nums[i:i + k + 1]))
            if i + k + 1 < n:
                max_sum = max(max_sum, sum(nums[i + 1:i + k + 2]))
        return max_sum