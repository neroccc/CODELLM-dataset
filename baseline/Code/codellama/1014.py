from typing import List
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_val = values[0]
        ans = 0
        for i in range(1, len(values)):
            ans = max(ans, max_val + values[i] - i)
            max_val = max(max_val, values[i] + i)
        return ans