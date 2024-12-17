from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = nums[i]
            ans = [dp[i][i], i]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                dp[i][j] = max(nums[i], nums[i] + dp[i + 1][j])
                dp[i][j] = max(dp[i][j], nums[j], nums[j] + dp[i + 1][j - 1])
                ans = [dp[i][j], i]

        i, j = ans
        return dp[i][j]