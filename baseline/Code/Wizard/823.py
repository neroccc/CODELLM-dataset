from typing import List
class Solution:
    def num_trees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                for k in range(j + 1, i):
                    if arr[j] * arr[k] > arr[i]:
                        break
                    dp[i] += dp[j] * dp[k]
                    dp[i] %= MOD

        return dp[n]