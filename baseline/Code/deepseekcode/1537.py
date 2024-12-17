from typing import List
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        sum1 = sum2 = 0
        while i < len(nums1) or j < len(nums2):
            if i < len(nums1) and (j == len(nums2) or nums1[i] < nums2[j]):
                sum1 += nums1[i]
                i += 1
            elif j < len(nums2) and (i == len(nums1) or nums1[i] > nums2[j]):
                sum2 += nums2[j]
                j += 1
            else:
                sum1 = sum2 = max(sum1, sum2) + nums1[i]
                i += 1
                j += 1
        return max(sum1, sum2) % (10**9 + 7)