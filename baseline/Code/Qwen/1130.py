from typing import List
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = arr[i]

        for diff in range(1, n):
            for i in range(n - diff):
                j = i + diff
                dp[i][j] = min(dp[i][k] + dp[k + 1][j] for k in range(i, j)) + max(arr[i:j + 1])

        return dp[0][n - 1]