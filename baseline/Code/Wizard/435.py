from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        end = intervals[0][1]
        count = 1
        for i in range(1, n):
            if intervals[i][0] >= end:
                count += 1
                end = intervals[i][1]
            else:
                end = min(end, intervals[i][1])
        return n - count