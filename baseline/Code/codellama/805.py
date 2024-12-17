from typing import List
class Solution:
    def canBeEqual(self, nums1: List[int], nums2: List[int]) -> bool:
        return sorted(nums1) == sorted(nums2)