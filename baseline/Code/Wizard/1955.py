from typing import List
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = 1
        for i in range(1, n):
            for j in range(3):
                dp[i][j] = dp[i - 1][j]
                if nums[i] == j:
                    dp[i][j] += dp[i - 1][j - 1]
                dp[i][j] %= MOD
        return dp[-1][2]