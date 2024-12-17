from typing import List
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        bits = len(bin(n)) - 2
        return (1 << bits) - 1 - self.minimumOneBitOperations(n ^ (1 << (bits - 1)))