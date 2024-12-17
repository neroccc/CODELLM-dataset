from typing import List
class Solution:
    def maxSlices(self, slices: List[int]) -> int:
        n = len(slices)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = slices[i]
        
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                dp[i][j] = max(slices[i] + dp[i + 1][j], slices[j] + dp[i][j - 1])
        
        return dp[0][n - 1]