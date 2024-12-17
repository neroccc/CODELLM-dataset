from typing import List
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            j = 1
            while j * j <= i and not dp[i]:
                dp[i] = not dp[i - j * j]
                j += 1
        return dp[-1]