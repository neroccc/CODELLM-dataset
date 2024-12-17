from typing import List
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        ans = 0

        for i in range(n1):
            for j in range(n2):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 2
                    ans = max(ans, dp[i + 1][j + 1])

        return ans