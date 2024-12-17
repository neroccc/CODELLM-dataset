from typing import List
class Solution:
    def maxAverageSubarrayI(self, nums: List[int], k: int) -> float:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                dp[i][j] = max(nums[i], dp[i + 1][j], dp[i][j - 1] + nums[j])

        return dp[0][n - 1] / k