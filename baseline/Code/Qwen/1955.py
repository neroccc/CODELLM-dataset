from typing import List
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        dp = [0] * 3
        for num in nums:
            dp[num] += 1
            for i in range(2):
                dp[i + 1] += dp[i]
        return dp[2] % MOD