from typing import List
class Solution:
    def minDays(self, n: int) -> int:
        dp = {0: 0, 1: 1, 2: 2}

        def dfs(n):
            if n in dp:
                return dp[n]

            dp[n] = min(n % 2 + dfs(n // 2), n % 3 + dfs(n // 3)) + 1
            return dp[n]

        return dfs(n)