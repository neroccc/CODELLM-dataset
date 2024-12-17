from typing import List
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if n == 0:
            return 1
        if k == 0 or maxPts == 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            if i < k:
                dp[i] = dp[i - 1] * (maxPts - 1) / maxPts
            else:
                dp[i] = dp[i - 1] * (maxPts - 1) / maxPts + dp[i - k] * k / maxPts
        return dp[n]