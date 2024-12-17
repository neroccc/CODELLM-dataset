from typing import List
class Solution:
    def minDays(self, n: int) -> int:
        if n == 1:
            return 1
        if n % 2 == 0:
            return n // 2
        if n % 3 == 0:
            return 2 * (n // 3)
        return n