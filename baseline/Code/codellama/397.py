from typing import List
class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while n != 1:
            if n & 1:
                n += 1 if n & 2 else -1
            else:
                n >>= 1
            ans += 1
        return ans
