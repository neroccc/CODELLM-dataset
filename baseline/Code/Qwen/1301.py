from typing import List
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        dp[n - 1][n - 1] = [0, 1]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == "X":
                    continue
                if i < n - 1:
                    dp[i][j][0] = max(dp[i][j][0], dp[i + 1][j][0])
                    dp[i][j][1] = (dp[i][j][1] + dp[i + 1][j][1]) % (10 ** 9 + 7)
                if j < n - 1:
                    dp[i][j][0] = max(dp[i][j][0], dp[i][j + 1][0])
                    dp[i][j][1] = (dp[i][j][1] + dp[i][j + 1][1]) % (10 ** 9 + 7)
                if i < n - 1 and j < n - 1:
                    dp[i][j][0] = max(dp[i][j][0], dp[i + 1][j + 1][0])
                    dp[i][j][1] = (dp[i][j][1] + dp[i + 1][j + 1][1]) % (10 ** 9 + 7)
                if board[i][j].isdigit():
                    dp[i][j][0] += int(board[i][j])

        return dp[0][0] if dp[0][0][0] > 0 else [0, 0]