import bisect
from typing import List
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        n = len(arr2)
        dp = {float('-inf'): 0}

        for a in arr1:
            new_dp = {}
            for prev, cnt in dp.items():
                if a > prev:
                    new_dp[a] = min(new_dp.get(a, float('inf')), cnt)
                idx = bisect.bisect_right(arr2, prev)
                if idx < n:
                    new_dp[arr2[idx]] = min(new_dp.get(arr2[idx], float('inf')), cnt + 1)
            dp = new_dp
            if not dp:
                return -1

        return min(dp.values())