from typing import List
class Solution:
    def maxEvents(self, events: List[List[int]], k: int) -> int:
        events.sort(key = lambda x: x[1])
        events.sort(key = lambda x: x[0])
        n = len(events)
        dp = [0] * n
        ans = 0
        for i in range(n):
            if dp[i] < k:
                dp[i + 1] = dp[i] + 1
                ans += events[i][2]
        return ans