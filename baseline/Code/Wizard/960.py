from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        dp = [[False] * m for _ in range(m)]
        for i in range(m):
            dp[i][i] = True

        for diff in range(1, m):
            for i in range(m - diff):
                j = i + diff
                for k in range(i, j):
                    if strs[0][k] <= strs[0][k + 1] and strs[n - 1][k] <= strs[n - 1][k + 1]:
                        dp[i][j] = True
                        break

        for i in range(1, n):
            for j in range(m):
                for k in range(j + 1):
                    if strs[i][k] < strs[i][k + 1] and dp[k][j]:
                        dp[k][j] = False
                        break

        count = 0
        for i in range(m):
            if not dp[i][m - 1]:
                count += 1

        return count