from typing import List
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10

        ans = 10
        for i in range(2, n + 1):
            ans *= 9 - (i - 1)
        return ans + 1