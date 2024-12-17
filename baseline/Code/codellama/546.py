from typing import List
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i][1] = (boxes[i] - 1) ** 2

        for l in range(2, n):
            for i in range(n - l):
                j = i + l - 1
                for k in range(i, j + 1):
                    dp[i][j][k - i + 1] = max(dp[i][k][k - i + 1] + dp[k + 1][j][k - i + 1] + (boxes[i] + boxes[k]) * (k - i + 1), dp[i][j][k - i])

        return dp[0][n - 1][n]