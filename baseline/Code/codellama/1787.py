from typing import List
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[float('inf')] * n for _ in range(1 << k)]
        for i in range(n):
            dp[1 << (i % k)][i] = 0
        for mask in range(1 << k):
            for i in range(n):
                if mask & 1 << i:
                    for j in range(n):
                        dp[mask][j] = min(dp[mask][j], dp[mask ^ 1 << i][j])
                    dp[mask][i] += 1
        return min(dp[-1])