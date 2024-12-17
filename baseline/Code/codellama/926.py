from typing import List
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        ans = 0

        for i in range(n):
            if s[i] == '1':
                dp[i] = dp[i - 1] + 1 if i > 0 else 1
            else:
                dp[i] = dp[i - 1]

        return n - max(dp)