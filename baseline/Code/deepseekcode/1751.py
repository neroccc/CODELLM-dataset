from typing import List
from deepseekcode.help.helphelp import get_last_event

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: (x[1], -x[2], x[0]))
        dp = [[0] * (k + 1) for _ in range(len(events) + 1)]
        for i in range(1, len(events) + 1):
            for j in range(1, k + 1):
                dp[i][j] = max(dp[i - 1][j], dp[get_last_event(events, i - 1)][j - 1] + events[i - 1][2])
        return dp[-1][-1]