from typing import List
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        dp = [[0] * len(cuts) for _ in range(len(cuts))]

        for i in range(len(cuts) - 2, -1, -1):
            for j in range(i + 2, len(cuts)):
                dp[i][j] = float("inf")
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])

        return dp[0][len(cuts) - 1]