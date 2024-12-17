from typing import List
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[2])
        events.sort(key=lambda x: x[1])
        n = len(events)
        count = 0
        i = 0
        j = 0
        ans = 0
        while i < n and count < k:
            if events[i][0] >= j:
                ans += events[i][2]
                j = events[i][1]
                count += 1
            i += 1
        return ans