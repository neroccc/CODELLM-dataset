from typing import List
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        ans = 0

        for i in range(n):
            dp[i][i] = 1
            ans += 1

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    ans += dp[i][j]

        return ans % (10 ** 9 + 7)