from typing import List
class Solution:
    def isWin(self, n: int) -> bool:
        while n % 4 == 0:
            n //= 4

        return n % 2 == 0