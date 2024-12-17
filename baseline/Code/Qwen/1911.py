from typing import List
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            dp[i][0] = max(dp[i + 1][1] + nums[i], dp[i + 1][0])
            dp[i][1] = max(dp[i + 1][0] - nums[i], dp[i + 1][1])

        return max(dp[0][0], dp[0][1])