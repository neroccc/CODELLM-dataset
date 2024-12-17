from typing import List
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        total = 0
        count = 0
        for x in satisfaction:
            if x <= 0:
                break
            total += x
            count += 1
        return total if total > 0 else 0