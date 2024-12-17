from typing import List
class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        a = b = c = 6
        if n == 1:
            return 12
        for _ in range(2, n + 1):
            a, b, c = b, c, (a + b + c) % mod
        return c