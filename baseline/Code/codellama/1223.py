from typing import List
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * 6 for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(6):
                for k in range(j + 1):
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
        ans = 0
        for i in range(6):
            ans = (ans + dp[n][i] * rollMax[i]) % MOD
        return ans
