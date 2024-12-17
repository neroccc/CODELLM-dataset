from typing import List
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [1] * n
        for i in range(1, n):
            if s[i] == 'I':
                dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % mod
            else:
                dp[i] = dp[i - 1]
        return dp[-1] % mod