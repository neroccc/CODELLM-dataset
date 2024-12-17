from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        nums = [1] + nums + [1]

        for diff in range(2, n + 1):
            for i in range(n - diff + 1):
                j = i + diff - 1
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])

        return dp[0][n - 1]