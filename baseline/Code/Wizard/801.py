from typing import List
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        count = 0
        for i in range(n):
            if nums1[i] > nums2[i]:
                nums1[i], nums2[i] = nums2[i], nums1[i]
                count += 1
            elif nums1[i] == nums2[i]:
                count += 1
        return count