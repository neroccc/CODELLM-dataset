from typing import List
class Solution:
    def isFibonacci(self, num: int) -> bool:
        a, b = 0, 1
        while b <= num:
            if b == num:
                return True
            a, b = b, a + b
        return False