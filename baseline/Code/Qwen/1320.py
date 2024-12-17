from typing import List
class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        dp = [[0] * 26 for _ in range(26)]

        for i in range(n - 1):
            c1 = ord(word[i]) - ord('A')
            c2 = ord(word[i + 1]) - ord('A')
            for j in range(26):
                dp[c1][c2] = min(dp[c1][c2], dp[c1][j] + abs(c1 - c2) + abs(j - c2))

        return min(dp[ord(word[-1]) - ord('A')])