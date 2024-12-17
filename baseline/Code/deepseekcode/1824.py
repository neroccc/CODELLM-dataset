from typing import List
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles) - 1
        dp = [[0] * 4 for _ in range(n + 1)]
        dp[0][2] = 0

        for i in range(1, n + 1):
            for j in range(1, 4):
                if j == obstacles[i]:
                    dp[i][j] = float('inf')
                else:
                    dp[i][j] = dp[i - 1][j]

            if dp[i][1] == dp[i][2] == dp[i][3] == float('inf'):
                return -1

            if dp[i][1] == float('inf'):
                dp[i][1] = min(dp[i - 1][2], dp[i - 1][3]) + 1
            if dp[i][2] == float('inf'):
                dp[i][2] = min(dp[i - 1][1], dp[i - 1][3]) + 1
            if dp[i][3] == float('inf'):
                dp[i][3] = min(dp[i - 1][1], dp[i - 1][2]) + 1

        return min(dp[-1])