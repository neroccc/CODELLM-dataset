from typing import List
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        dp = [[0]*n for _ in range(m)]
        dp[startRow][startColumn] = 1
        move = [(0,1),(0,-1),(-1,0),(1,0)]
        for _ in range(maxMove):
            dp2 = [[0]*n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    for dr, dc in move:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            dp2[r][c] = (dp2[r][c] + dp[nr][nc]) % MOD
                        else:
                            dp2[r][c] = (dp2[r][c] + 1) % MOD
            dp = dp2
        return sum(sum(row) for row in dp) % MOD