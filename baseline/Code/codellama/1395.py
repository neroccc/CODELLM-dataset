from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1):
            if points[i][0] == points[i + 1][0] and points[i][1] == points[i + 1][1]:
                dp[i][i + 1] = 1
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    dp[i][j] = 1
                else:
                    max_ = 0
                    for k in range(i, j + 1):
                        max_ = max(max_, dp[i][k] + dp[k + 1][j])
                    dp[i][j] = max_
        return dp[0][n - 1]
