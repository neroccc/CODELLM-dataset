from typing import List
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * (i - 1) % MOD

        for i in range(2, n + 1):
            dp[i] = (dp[i] + dp[i - 1] * (i - 1)) % MOD

        return dp[n] if n == k else (dp[n] - dp[n - 1] * (n - k) % MOD) % MOD