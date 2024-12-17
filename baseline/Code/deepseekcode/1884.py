from typing import List
class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [0, 1, 2] + [0] * (n - 2)
        for i in range(3, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = min(dp[i], max(dp[j - 1], dp[i - j]) + 1)
        return dp[n]