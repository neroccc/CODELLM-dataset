from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        i = 0
        for i in range(n):
            if i > max_reach:
                return False
            if i + nums[i] > max_reach:
                max_reach = i + nums[i]
        return True