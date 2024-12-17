from typing import List
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        max_val = values[0]
        ans = 0

        for i in range(1, n):
            ans = max(ans, values[i] + max_val - i)
            max_val = max(max_val, values[i] + i)

        return ans