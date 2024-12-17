from typing import List
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp0, dp1, dp0_max = arr[0], 0, arr[0]
        for i in range(1, n):
            dp1 = max(dp0, dp1 + arr[i])
            dp0 = max(dp0, 0) + arr[i]
            dp0_max = max(dp0_max, dp0)
        return max(dp0_max, dp1)