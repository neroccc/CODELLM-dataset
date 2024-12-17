from typing import List
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(minProfit + 1):
                dp[i + 1][j] += dp[i][j]
                if j >= profit[i]:
                    dp[i + 1][j] += group[i] * dp[i][j - profit[i]]
        return sum(dp[-1]) % (10 ** 9 + 7)
