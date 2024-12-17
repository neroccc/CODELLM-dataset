from typing import List
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        swap = [float('inf')] * n
        same = [0] * n
        
        for i in range(n):
            if nums1[i] < nums2[i]:
                swap[i] = 1
            elif nums1[i] > nums2[i]:
                swap[i] = 0
            else:
                same[i] = 1
                
        for i in range(1, n):
            if swap[i - 1] == 1:
                swap[i] = min(swap[i], same[i - 1] + 1)
            if same[i - 1] == 1:
                same[i] = min(same[i], swap[i - 1] + 1)
                
        return min(swap[-1], same[-1])