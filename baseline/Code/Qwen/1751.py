from typing import List
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n)]

        for i in range(n):
            dp[i][1] = events[i][2]

        for i in range(1, n):
            for j in range(2, k + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + events[i][2])
                for p in range(i - 1, -1, -1):
                    if events[p][1] < events[i][0]:
                        dp[i][j] = max(dp[i][j], dp[p][j - 1] + events[i][2])
                        break

        return max(dp[n - 1])