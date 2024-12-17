from typing import List
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1):
            dp[i][i + 1] = nums[i] * nums[i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                dp[i][j] = max(nums[i] * nums[k] * nums[j] + dp[i][k] for k in range(i + 1, j))

        return dp[0][n - 1]