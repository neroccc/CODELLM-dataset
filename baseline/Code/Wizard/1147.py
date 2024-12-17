from typing import List
class Solution:
    def longestSubstring(self, text: str) -> int:
        n = len(text)
        dp = [0] * n
        dp[0] = 1
        max_len = 1
        for i in range(1, n):
            dp[i] = 1
            j = 0
            while j < i:
                if text[i] == text[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                j += 1
            max_len = max(max_len, dp[i])
        return n // max_len