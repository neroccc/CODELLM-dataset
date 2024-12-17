from typing import List
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n == 0:
            return 1.0

        if k == 1:
            return 1.0 * min(n, maxPts) / maxPts

        dp = [0] * (k + 1)
        dp[0] = 1.0
        for i in range(1, k + 1):
            dp[i] = 1.0 * min(n, maxPts) / maxPts

        for i in range(1, n + 1):
            new_dp = [0] * (k + 1)
            for j in range(k + 1):
                if j < i:
                    new_dp[j] = dp[j]
                else:
                    new_dp[j] = dp[j - 1] - dp[j - i]
                    if j - i < k:
                        new_dp[j] += dp[j - i]
                    new_dp[j] /= maxPts
            dp = new_dp

        return sum(dp)