from typing import List
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        mod = 10**9 + 7
        max_sum = 0

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                max_sum += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                max_sum += nums2[j]
                j += 1
            else:
                max_sum += nums1[i]
                i += 1
                j += 1

        while i < n1:
            max_sum += nums1[i]
            i += 1

        while j < n2:
            max_sum += nums2[j]
            j += 1

        return max_sum % mod