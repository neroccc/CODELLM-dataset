from typing import List
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if seats[0][0] == '.' else 0

        for i in range(1, n):
            if seats[0][i] == '.':
                dp[0][i] = dp[0][i - 1]

        for i in range(1, m):
            for j in range(n):
                if seats[i][j] == '.':
                    dp[i][j] = dp[i - 1][j]
                    if j > 0 and seats[i - 1][j - 1] == '.':
                        dp[i][j] += dp[i - 1][j - 1]
                    if j < n - 1 and seats[i - 1][j + 1] == '.':
                        dp[i][j] += dp[i - 1][j + 1]

        return max(dp[-1])