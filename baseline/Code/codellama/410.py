from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[float("inf")] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + nums[i - 1])
        return dp[n][k]