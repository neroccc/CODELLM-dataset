from typing import List
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        dp = [[float('inf')] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(n):
            for j in range(target + 1):
                if j >= stations[i][0]:
                    dp[i + 1][j] = min(dp[i][j], dp[i][j - stations[i][0]] + stations[i][1])

        for j in range(startFuel, target + 1):
            if dp[n][j] != float('inf'):
                return n - dp[n].index(j)
        return -1