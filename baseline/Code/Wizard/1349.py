from typing import List
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        dp = [[0] * n for _ in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):
                if seats[i][j] == '.':
                    dp[i][j] = 1
                    if i > 0 and seats[i - 1][j] == '.':
                        dp[i][j] += dp[i - 1][j]
                    if j > 0 and seats[i][j - 1] == '.':
                        dp[i][j] += dp[i][j - 1]
                    if i > 0 and j > 0 and seats[i - 1][j - 1] == '.':
                        dp[i][j] += dp[i - 1][j - 1]
                    ans = max(ans, dp[i][j])

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if seats[i][j] == '.':
                    dp[i][j] = 1
                    if i < m - 1 and seats[i + 1][j] == '.':
                        dp[i][j] += dp[i + 1][j]
                    if j < n - 1 and seats[i][j + 1] == '.':
                        dp[i][j] += dp[i][j + 1]
                    if i < m - 1 and j < n - 1 and seats[i + 1][j + 1] == '.':
                        dp[i][j] += dp[i + 1][j + 1]
                    ans = max(ans, dp[i][j])

        return ans