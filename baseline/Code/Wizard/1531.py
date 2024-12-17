from typing import List
class Solution:
    def minDeletionSize(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(n):
            dp[i] = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i] = min(dp[i], dp[j] + 1)

        ans = 0
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i + 1] = dp[i] + 1

        for i in range(n - 1):
            ans += dp[i]
            if ans > k:
                k -= dp[i]
                ans -= dp[i]
                if k == 0:
                    break

        return ans