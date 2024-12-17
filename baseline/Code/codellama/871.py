from typing import List
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = i
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i - 1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j - 1 >= 0 and stations[i - 1][0] <= startFuel + stations[j - 1][0]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
        i, j = n, 0
        while i >= 0 and j < n:
            if dp[i][j] > dp[i][j + 1]:
                j += 1
            else:
                i -= 1
        return -1 if i < 0 else dp[i][j]
