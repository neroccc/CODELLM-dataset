from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        dp = [[False] * m for _ in range(n)]
        ans = 0

        for i in range(n):
            for j in range(m - 1):
                if strs[i][j] > strs[i][j + 1]:
                    dp[i][j] = True
                    ans += 1

        for i in range(m - 1):
            for j in range(n - 1):
                if strs[j][i] > strs[j + 1][i]:
                    dp[j][i] = True
                    ans += 1

        return ans