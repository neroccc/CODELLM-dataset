from typing import List
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = nums[0]
        for i in range(1, n):
            dp[i][i] = nums[i]
            dp[i - 1][i] = max(dp[i - 1][i - 1], nums[i])
            for j in range(i - 1):
                dp[j][i] = max(dp[j][i], dp[j + 1][i], dp[j][i - 1] + nums[j])
        return dp[0][-1]