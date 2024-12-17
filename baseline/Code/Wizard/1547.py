from typing import List
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = float('inf')
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            for cut in cuts:
                if cut < i:
                    dp[i] = min(dp[i], dp[cut] + (i - cut))

        return dp[n]