from typing import List
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        res, total = 0, 0
        while satisfaction and satisfaction[-1] < 0:
            total += satisfaction.pop()
        while satisfaction:
            total += satisfaction.pop()
            res += total
        return res