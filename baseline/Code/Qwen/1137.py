from typing import List
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            t0, t1, t2 = 0, 1, 1
            for _ in range(n - 2):
                t0, t1, t2 = t1, t2, t0 + t1 + t2
            return t2