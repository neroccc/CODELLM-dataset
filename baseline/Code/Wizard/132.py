from typing import List
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        cut = [0] * n

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                cut[i + 1] = 0

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j]:
                    dp[i][j] = True
                    cut[j] = cut[i]
                else:
                    cut[j] = cut[i] + 1
                    for k in range(i + 1, j):
                        if s[i] == s[k] and dp[i + 1][j - 1]:
                            dp[i][j] = True
                            cut[j] = min(cut[j], cut[i] + 1)

        return cut[n - 1]