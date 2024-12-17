from typing import List
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        mod = 10 ** 9 + 7

        for i in range(1, n + 1):
            for j in range(i):
                if s[j:i].startswith("0"):
                    break
                num = int(s[j:i])
                if num > k:
                    break
                dp[i] = (dp[i] + dp[j]) % mod

        return dp[n]