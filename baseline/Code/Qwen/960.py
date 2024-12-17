from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[i][j] = 1
                else:
                    if strs[i][j] > strs[i - 1][j]:
                        dp[i][j] = dp[i - 1][j] + 1
                    else:
                        dp[i][j] = dp[i - 1][j]

        return m - max(dp[-1])