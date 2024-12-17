from typing import List
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        if n == 2:
            return 9 * 9

        count = 9 * 9
        for i in range(3, n + 1):
            count *= 9 - i + 1

        return count