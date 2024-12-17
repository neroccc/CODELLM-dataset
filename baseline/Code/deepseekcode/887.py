from typing import List
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
        m = 0
        while dp[k][m] < n:
            m += 1
            for k in range(1, k+1):
                dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1
        return m