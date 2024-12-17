from typing import List
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        ans = 0
        mx = values[0]

        for i in range(1, n):
            ans = max(ans, mx + values[i] - i)
            mx = max(mx, values[i] + i)

        return ans