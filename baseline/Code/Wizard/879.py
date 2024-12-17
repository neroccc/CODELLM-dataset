from typing import List
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(minProfit + 1)]
        dp[0][0] = 1

        for p in profit:
            for j in range(n, 0, -1):
                for i in range(minProfit, -1, -1):
                if i >= p:
                    dp[i][j] += dp[i - p][j - 1]
                    if j >= group[p]:
                        dp[i][j] += dp[i][j - group[p]]
                    dp[i][j] %= MOD

        return dp[minProfit][n]