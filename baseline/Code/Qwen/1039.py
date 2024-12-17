from typing import List
class Solution:
    def maxScore(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                dp[i][j] = max(
                    values[i] + min(dp[i + 1][j - 1], dp[i + 2][j]),
                    values[j] + min(dp[i + 1][j - 1], dp[i][j - 2]),
                )

        return dp[0][n - 1] // 2