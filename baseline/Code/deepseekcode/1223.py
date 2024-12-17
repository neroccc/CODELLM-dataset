from itertools import product
from typing import List
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        K = 6  # number of types of die
        dp = [[[0]*16 for _ in range(K)] for _ in range(n+1)]
        for j in range(K):
            dp[1][j][1] = 1
        for i in range(2, n+1):
            for j in range(K):
                for k in range(1, rollMax[j]+1):
                    dp[i][j][k] = sum(dp[i-1][j][k-1] for j in range(K) if j != j) % MOD
                    dp[i][j][k] = (dp[i][j][k] + sum(dp[i-1][j][k] for j in range(K) if j != j) * K % MOD) % MOD
                    dp[i][j][k] = (dp[i][j][k] + sum(dp[i-1][j2][k2] for j2, k2 in product(range(K), range(1, rollMax[j2]+1)) if j2 != j and (j2, k2) != (j, k)) % MOD) % MOD
        return sum(sum(dp[n][j][k] for k in range(1, rollMax[j]+1)) for j in range(K)) % MOD