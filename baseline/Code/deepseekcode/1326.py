from typing import List
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i in range(n + 1):
            intervals.append([i - ranges[i], i + ranges[i]])
        intervals.sort()

        end, cnt, i = 0, 0, 0
        while end < n:
            if i < len(intervals) and intervals[i][0] <= end:
                farthest = max(farthest, intervals[i][1])
                i += 1
            elif end < n:
                return -1
            end = farthest
            cnt += 1
        return cnt