from typing import List
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            c = bin(mask).count('1')
            if c % 2 == 1: continue
            for i in range(n):
                if (mask >> i) & 1:
                    dp[mask] = min(dp[mask], dp[mask ^ (1 << i)] + (nums1[c // 2] ^ nums2[i]))

        return dp[-1]