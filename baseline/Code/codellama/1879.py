from typing import List
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        return sum(nums) & 1 == 0
