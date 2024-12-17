from typing import List
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        dp = [[[-1, 0] for _ in range(n+1)] for _ in range(n+1)]
        dp[n-1][n-1] = [0, 1]
        for i in range(n-2, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] == 'X': continue
                if board[i][j] == 'S': dp[i][j] = dp[i+1][j][0] if dp[i+1][j][0] > dp[i][j+1][0] else dp[i][j+1][0]
                if dp[i][j] == 'E': dp[i][j] = dp[i+1][j][0] if dp[i+1][j][0] > dp[i][j+1][0] else dp[i][j+1][0]
                if dp[i][j] == 'E': dp[i][j] = dp[i+1][j][0] if dp[i+1][j][0] > dp[i][j+1][0] else dp[i][j+1][0]
                if dp[i][j] == 'E': dp[i][j] = dp[i+1][j][0] if dp[i+1][j][0] > dp[i][j+1][0] else dp[i][j+1][0]
                if dp[i][j] == 'E': dp[i][j] = dp[i+1][j][0] if dp[i+1][j][0] > dp[i][j+1][0] else dp[i][j+1][0]
                if dp[i][j] == 'E': dp[i