from typing import List
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10**9 + 7
        n = len(binary)
        dp = [0]*2 + [1]*n
        for i in range(2, n+1):
            if binary[i-1] == '1':
                dp[i] = (dp[i-1]*2 + 1) % MOD
            else:
                dp[i] = (dp[i-1]*2) % MOD
        return (sum(dp) - binary.count('0')*2) % MOD