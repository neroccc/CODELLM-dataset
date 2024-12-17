from typing import List
class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            while i > 0:
                count += i // 10
                i //= 10
        return count