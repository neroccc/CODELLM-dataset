from typing import List
class Solution:
    def shortestCommonSupersequence(self, words: List[str]) -> str:
        n = len(words)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if words[i - 1][j - 1] == words[i - 1][j - 2]:
                    dp[i][j] = dp[i - 1][j - 2] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return "".join(words[i - 1][:dp[i][j]] for i, j in itertools.product(range(1, n + 1), range(1, n + 1)))