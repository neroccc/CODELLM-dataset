from typing import List
class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        dp = [[0] * n for _ in range(n)]
        ans = 0

        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 1):
            if text[i] == text[i + 1]:
                dp[i][i + 1] = 2
                ans += 1

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if text[i] == text[j] and dp[i + 1][j - 1]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    ans += 1

        return ans