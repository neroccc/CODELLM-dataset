from typing import List
class Solution:
    def maxPoints(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            dp[i] = [0] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]