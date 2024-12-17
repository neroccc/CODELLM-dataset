from typing import List
class Solution:
    def countGoodSubsequences(self, binary: str) -> int:
        n = len(binary)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            if binary[i] == "1":
                dp[i] = dp[i - 1] + 1
            dp[i] += dp[i - 1]
        return dp[-1] % (10 ** 9 + 7)
