from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                for x in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[x][j - 1], sum(nums[x:i])))

        return dp[n][k]