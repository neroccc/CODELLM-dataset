from typing import List
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * k for k in range(1, 101)]
        dp[0][0] = poured
        for i in range(1, 101):
            for j in range(i + 1):
                if dp[i - 1][j] > 1:
                    dp[i][j] += (dp[i - 1][j] - 1) / 2
                    dp[i][j + 1] += (dp[i - 1][j] - 1) / 2
        return min(1, dp[query_row][query_glass])