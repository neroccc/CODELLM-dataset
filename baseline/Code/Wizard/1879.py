from typing import List
class Solution:
    def minXorSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums2.sort()
        nums1.sort()
        xor_sum = 0
        for i in range(len(nums1)):
            xor_sum += nums1[i] ^ nums2[i]
        return xor_sum