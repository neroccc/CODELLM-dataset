from typing import List
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        keep = [n] * n
        swap = [n] * n
        keep[0] = 0
        swap[0] = 1
        for i in range(1, n):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                keep[i] = keep[i - 1]
                swap[i] = swap[i - 1] + 1
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                keep[i] = min(keep[i], swap[i - 1])
                swap[i] = min(swap[i], keep[i - 1] + 1)
        return min(keep[-1], swap[-1])