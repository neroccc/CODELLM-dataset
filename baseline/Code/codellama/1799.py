from math import gcd
from typing import List
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums) // 2
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[2 * i]
        for diff in range(1, n):
            for i in range(n - diff):
                j = i + diff
                dp[i][j] = max(nums[2 * i] * gcd(nums[2 * i + 1], nums[2 * j + 1]), dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]