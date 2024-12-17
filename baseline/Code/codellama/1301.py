from typing import List
class Solution:
    def maxSum(self, board: List[str]) -> List[int]:
        m, n = len(board), len(board[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'S':
                    dp[i][j] = 1
                elif board[i][j] != 'X':
                    dp[i][j] = int(board[i][j])
                    if i < m - 1:
                        dp[i][j] += dp[i + 1][j]
                    if j < n - 1:
                        dp[i][j] += dp[i][j + 1]
        return [sum(dp[0]), dp[0][0]]