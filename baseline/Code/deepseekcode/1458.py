from math import inf
from typing import List
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[-inf] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = max(
                    nums1[i] * nums2[j] + max(0, dp[i + 1][j + 1]),
                    dp[i + 1][j],
                    dp[i][j + 1]
                )
        return max(0, dp[0][0])