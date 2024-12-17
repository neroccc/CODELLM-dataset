from typing import List
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        max_len = 0

        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1 - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                max_len = max(max_len, dp[i])

        return max_len