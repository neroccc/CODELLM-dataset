from typing import List
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)
        n = len(s)
        dp = [[0] * 10 for _ in range(n)]
        dp[0][0] = 1
        for i in range(1, n):
            dp[i][0] = 1
            for j in range(1, 10):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

        ans = 0
        for i in range(n):
            ans += dp[n - i - 1][int(s[i])]
            if i == 0:
                continue
            for j in range(int(s[i])):
                ans += dp[n - i - 1][j]
            if s[i] == s[i - 1]:
                break

        return n - i - 1 + ans