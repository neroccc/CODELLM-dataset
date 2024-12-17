from typing import List
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (K + 1) for _ in range(N + 1)]

        for n in range(1, N + 1):
            for k in range(1, K + 1):
                dp[n][k] = dp[n - 1][k - 1] + dp[n - 1][k] + 1

            if dp[n][K] >= N:
                return n

        return N