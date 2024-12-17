from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            for j in range(i - 1, -1, -1):
                if stones[i] - stones[j] <= n - 1:
                    dp[stones[i]] = dp[j] or dp[stones[i] - stones[j] - 1] or dp[stones[i] - stones[j] + 1]

        return dp[-1]