from typing import List
class Solution:
    def uniqueBuildings(self, prevRoom: List[int]) -> int:
        n = len(prevRoom)
        dp = [1] * n
        mod = 10**9 + 7

        for i in range(1, n):
            dp[i] = dp[prevRoom[i]] + (i != prevRoom[i])
            dp[i] %= mod

        return sum(dp) % mod