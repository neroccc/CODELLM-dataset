from typing import List
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = float('-inf')
        max_value = values[0]

        for i in range(1, len(values)):
            max_score = max(max_score, max_value + values[i] - i)
            max_value = max(max_value, values[i] + i)

        return max_score