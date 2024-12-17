from typing import List
class Solution:
    def numberOfWays(self, prevRoom: List[int]) -> int:
        n = len(prevRoom)
        dp = [1] * n
        for i in range(1, n):
            dp[i] = sum(dp[prevRoom[j]] for j in range(i) if prevRoom[j] != -1)
        return sum(dp) % (10**9 + 7)