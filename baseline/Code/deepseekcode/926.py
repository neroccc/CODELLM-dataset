from typing import List
class Solution:
    def minFlipsMonotoneIncreasing(self, s: str) -> int:
        n = len(s)
        dp0, dp1 = 0, 0
        for i in range(n):
            if s[i] == '0':
                dp0 += 1
            else:
                dp1 = min(dp0, dp1)
        return min(dp0, dp1)