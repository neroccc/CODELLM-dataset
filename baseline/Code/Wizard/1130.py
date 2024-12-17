from typing import List
class Solution:
    def minProductSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = arr[i]
            for j in range(i + 1, n):
                dp[i][j] = max(arr[i] * arr[j], dp[i + 1][j - 1])

        return dp[0][n - 1]