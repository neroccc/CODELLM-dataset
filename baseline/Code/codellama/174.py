from typing import List
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[float('inf')] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                if i == m - 1:
                    dp[i][j] = dp[i][j + 1] - dungeon[i][j]
                elif j == n - 1:
                    dp[i][j] = dp[i + 1][j] - dungeon[i][j]
                else:
                    dp[i][j] = max(dp[i + 1][j] - dungeon[i][j], dp[i][j + 1] - dungeon[i][j])
        return max(1, 1 - dp[0][0])