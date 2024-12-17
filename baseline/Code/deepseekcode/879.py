from typing import List
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        dp = [[0]*(n+1) for _ in range(minProfit+1)]
        dp[0][0] = 1
        for k in range(len(group)):
            g = group[k]
            p = profit[k]
            for i in range(minProfit, -1, -1):
                for j in range(n, g-1, -1):
                    dp[min(i+p, minProfit)][j-g] = (dp[min(i+p, minProfit)][j-g] + dp[i][j]) % MOD
        return sum(dp[minProfit][:n+1]) % MOD