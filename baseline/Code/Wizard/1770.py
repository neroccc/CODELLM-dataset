from typing import List
class Solution:
    def maxScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i == n - 1 and j == m - 1:
                    dp[i][j] = nums[i] * multipliers[j]
                elif i == n - 1:
                    dp[i][j] = max(dp[i + 1][j + 1], dp[i + 1][j]) + nums[i] * multipliers[j]
                elif j == m - 1:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                else:
                    dp[i][j] = max(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1]) + nums[i] * multipliers[j]

        return dp[0][0]