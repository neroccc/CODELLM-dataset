from typing import List
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [1]
        last = {}
        mod = 10**9 + 7
        for i, c in enumerate(s, 1):
            dp.append(dp[-1] * 2 % mod)
            if c in last:
                dp[-1] -= dp[last[c]]
            last[c] = i
        return (dp[-1]-1)%mod