from typing import List
class Solution:
    def stoneGameII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = stones[i]
        
        for diff in range(2, n + 1):
            for i in range(n - diff + 1):
                j = i + diff - 1
                dp[i][j] = max(stones[i] - dp[i + 1][j], stones[j] - dp[i][j - 1])
        
        return dp[0][n - 1]
