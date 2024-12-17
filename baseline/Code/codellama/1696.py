from typing import List
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = nums[0]
        for i in range(1, n):
            dp[i][i] = nums[i] + dp[i - 1][i - 1]

        for diff in range(2, n + 1):
            for i in range(n - diff + 1):
                j = i + diff - 1
                if j < n:
                    dp[i][j] = max(nums[i] + dp[i + 1][j], nums[j] + dp[i][j - 1])
                else:
                    dp[i][j] = nums[i] + dp[i + 1][j]

        return dp[0][n - 1]