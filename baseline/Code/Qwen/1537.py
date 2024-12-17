from typing import List
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        mod = 10 ** 9 + 7
        ans = 0
        sum1, sum2 = 0, 0

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                ans += max(sum1, sum2) + nums1[i]
                sum1, sum2 = 0, 0
                i += 1
                j += 1

        while i < n1:
            sum1 += nums1[i]
            i += 1

        while j < n2:
            sum2 += nums2[j]
            j += 1

        ans += max(sum1, sum2)
        return ans % mod