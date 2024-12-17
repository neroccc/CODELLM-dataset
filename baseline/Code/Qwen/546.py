from typing import List
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i][0] = (i + 1) ** 2

        for diff in range(1, n):
            for i in range(n - diff):
                j = i + diff
                for k in range(i, j + 1):
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i][k - 1][0] + dp[k + 1][j][k],
                    )
                if boxes[i] == boxes[j]:
                    dp[i][j][j] = max(
                        dp[i][j][j],
                        dp[i][j - 1][j - 1] + (j - i + 1) ** 2,
                    )

        return dp[0][n - 1][n - 1]