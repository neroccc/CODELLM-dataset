from typing import List
class Solution:
    def minOperations(self, n: int) -> int:
        count = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n -= 1
            count += 1
        return count