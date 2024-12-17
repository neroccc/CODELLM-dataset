from typing import List
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        dp = {-1: float('inf')}
        for i in arr1:
            dp = {i: min(v, dp[j] + 1) for j, v in dp.items() if i > v}
        return min(dp.values()) if dp else -1