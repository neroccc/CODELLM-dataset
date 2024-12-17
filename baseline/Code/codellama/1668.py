from typing import List
class Solution:
    def longestKRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][i] = 1

        for i in range(n - m + 1):
            for j in range(i, n):
                if sequence[i] == sequence[j] and dp[i + 1][j - 1]:
                    dp[i][j] = 1

        for i in range(m, n + 1):
            for j in range(i, n + 1):
                if dp[i - m][j - 1]:
                    return j - i + 1

        return 0