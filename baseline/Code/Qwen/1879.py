from typing import List
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[float('inf')] * (1 << n) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for mask in range(1 << n):
                for j in range(n):
                    if mask & (1 << j) == 0:
                        continue
                    dp[i][mask] = min(dp[i][mask], dp[i - 1][mask ^ (1 << j)] + (nums1[i - 1] ^ nums2[j]))

        return dp[n][(1 << n) - 1]