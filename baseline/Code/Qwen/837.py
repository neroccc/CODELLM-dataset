from typing import List
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        sum_dp = 1.0
        prob = 0.0

        for i in range(1, n + 1):
            dp[i] = sum_dp / maxPts
            if i < k:
                sum_dp += dp[i]
            if i - maxPts >= 0:
                sum_dp -= dp[i - maxPts]

        for i in range(k, n + 1):
            prob += dp[i]

        return prob