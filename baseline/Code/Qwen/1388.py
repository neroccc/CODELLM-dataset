from typing import List
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == 1:
                    dp[i][j] = max(dp[i][j - 1], slices[j - 1])
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 2] + slices[j - 1])

        return dp[n // 3][n]