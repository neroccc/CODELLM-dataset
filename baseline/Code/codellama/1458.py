from typing import List
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[0] * n for _ in range(n)]
        ans = float("-inf")

        for i in range(n):
            dp[i][i] = nums1[i] * nums2[i]
            ans = max(ans, dp[i][i])

        for diff in range(2, n + 1):
            for i in range(n - diff + 1):
                j = i + diff - 1
                dp[i][j] = nums1[i] * nums2[j] + dp[i + 1][j - 1]
                ans = max(ans, dp[i][j])

        return ans