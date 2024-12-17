from typing import List
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1.0
        elif n == 2:
            return 0.5
        else:
            return 0.5