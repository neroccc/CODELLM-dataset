from typing import List
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    left_score = prefix_sum[k + 1] - prefix_sum[i]
                    right_score = prefix_sum[j + 1] - prefix_sum[k + 1]
                    if left_score < right_score:
                        dp[i][j] = max(dp[i][j], dp[i][k] + left_score)
                    elif left_score > right_score:
                        dp[i][j] = max(dp[i][j], dp[k + 1][j] + right_score)
                    else:
                        dp[i][j] = max(dp[i][j], dp[i][k] + left_score, dp[k + 1][j] + right_score)

        return dp[0][n - 1]