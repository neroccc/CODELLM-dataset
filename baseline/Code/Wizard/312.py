from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                for i in range(left, right + 1):
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right + 1] + dp[left][i - 1] + dp[i + 1][right])

        return dp[0][n]