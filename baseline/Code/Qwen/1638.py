from typing import List
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0

        for i in range(n):
            for j in range(m):
                if s[i] == t[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    ans += dp[i][j]
                    dp[i + 1][j + 1] = 0

        return ans