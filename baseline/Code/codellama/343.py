from typing import List
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        res = [0] * (n + 1)
        res[2] = 1
        res[3] = 2
        for i in range(4, n + 1):
            res[i] = max(res[j] * res[i - j] for j in range(1, i))
        return res[n]