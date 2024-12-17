from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        def robRange(start: int, end: int) -> int:
            rob, no_rob = 0, 0
            for i in range(start, end):
                rob, no_rob = no_rob + nums[i], max(rob, no_rob)
            return max(rob, no_rob)
        
        return max(robRange(0, len(nums) - 1), robRange(1, len(nums)))