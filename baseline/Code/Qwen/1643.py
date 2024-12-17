from typing import List
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        row, col = destination
        n = row + col
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        dp[0][0] = 1

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        ans = []
        i, j = 0, 0
        while i < row and j < col:
            if k <= dp[i + 1][j]:
                ans.append("H")
                i += 1
            else:
                ans.append("V")
                k -= dp[i + 1][j]
                j += 1

        while i < row:
            ans.append("H")
            i += 1

        while j < col:
            ans.append("V")
            j += 1

        return "".join(ans)