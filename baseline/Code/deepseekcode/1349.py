from typing import List
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        seats = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if seats[i][j] == '.':
                    seats[i][j] = 0
                else:
                    seats[i][j] = 1
        
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = seats[i][0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], seats[i][j] + dp[i][j-1])
        
        for j in range(1, n):
            for i in range(1, m):
                dp[i][j] = max(dp[i][j-1], seats[i][j] + dp[i-1][j-1])
            for i in range(m-1, -1, -1):
                if i-1>=0:
                    dp[i][j] = max(dp[i][j], seats[i][j] + dp[i-1][j-1])
        
        return dp[-1][-1]