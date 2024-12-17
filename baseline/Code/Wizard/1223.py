from typing import List
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        dp = [1] * 6
        for _ in range(n - 1):
            new_dp = [0] * 6
            for i in range(6):
                for j in range(6):
                    if i == j:
                        new_dp[i] += dp[i]
                    elif rollMax[i] >= rollMax[j]:
                        new_dp[j] += dp[i]
            dp = new_dp
        return sum(dp) % MOD