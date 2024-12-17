from typing import List
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        dp = [[0] * 16 for _ in range(6)]
        for i in range(6):
            dp[i][1] = 1

        for i in range(1, n):
            temp = [[0] * 16 for _ in range(6)]
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    for l in range(6):
                        if j != l:
                            temp[j][k] += dp[l][k]
                        else:
                            temp[j][k] += dp[l][k - 1]
            dp = temp

        ans = 0
        for i in range(6):
            ans += sum(dp[i])
        return ans % MOD