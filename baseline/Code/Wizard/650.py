from typing import List
class Solution:
    def minOperations(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return (n // 2) * 2
        else:
            return (n // 2) * 2 + 1