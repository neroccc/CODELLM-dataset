from typing import List
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        m = len(s)
        dp = [0] * (m + 1)
        dp[0] = 1
        for i in range(1, m):
            dp[i] = dp[i - 1] * len(digits)
        for i in range(m):
            is_prefix = False
            for d in digits:
                if d < s[i]:
                    dp[m] += dp[i]
                elif d == s[i]:
                    is_prefix = True
                    dp[m] += dp[i]
                    break
            if not is_prefix:
                return dp[m]
        return dp[m] + 1