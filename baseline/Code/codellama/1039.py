from typing import List
class Solution:
    def minimumTimeRequired(self, values: List[int]) -> int:
        n = len(values)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                dp[i] = min(dp[i], dp[j] + abs(values[i] - values[j]))
        return dp[-1]