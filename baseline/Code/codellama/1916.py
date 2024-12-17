from typing import List
class Solution:
    def numberOfWays(self, prevRoom: List[int]) -> int:
        n = len(prevRoom)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = dp[prevRoom[i]] + dp[i - 1]
        return dp[-1] % (10 ** 9 + 7)
