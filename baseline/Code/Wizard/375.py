from typing import List
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for l in range(2, n + 1):
            for lo in range(n - l + 1):
                hi = lo + l - 1
                dp[lo][hi] = float('inf')
                for mid in range(lo, hi + 1):
                    dp[lo][hi] = min(dp[lo][hi], max(dp[lo][mid - 1], dp[mid + 1][hi]) + mid)

        return dp[1][n]