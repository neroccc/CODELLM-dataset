from typing import List
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        m = len(hats[0])
        dp = [[0] * m for _ in range(1 << m)]
        for i in range(m):
            dp[1 << i][i] = 1
        for i in range(n):
            for mask in range(1 << m):
                for j in range(m):
                    if mask & (1 << j):
                        for k in hats[i]:
                            if k == j + 1:
                                dp[mask | (1 << j)][j] += dp[mask][k - 1]
        return (dp[-1][m - 1] % (10 ** 9 + 7))