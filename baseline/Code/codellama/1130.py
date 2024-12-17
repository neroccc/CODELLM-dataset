from typing import List
class Solution:
    def minCameraCover(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[float("inf")] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = 1
                elif j == i:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1) + arr[i - 1]
        return dp[n][n]