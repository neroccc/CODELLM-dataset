from typing import List
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines = set(map(tuple, mines))
        dp = [[0] * n for _ in range(n)]
        ans = 0

        for i in range(n):
            cnt = 0
            for j in range(n):
                cnt = 0 if (i, j) in mines else cnt + 1
                dp[i][j] = cnt

            cnt = 0
            for j in range(n - 1, -1, -1):
                cnt = 0 if (i, j) in mines else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)

        for j in range(n):
            cnt = 0
            for i in range(n):
                cnt = 0 if (i, j) in mines else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)

            cnt = 0
            for i in range(n - 1, -1, -1):
                cnt = 0 if (i, j) in mines else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)
                ans = max(ans, dp[i][j])

        return ans