from typing import List
class Solution:
    def minOperations(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.minOperations(n // 2)
        else:
            return 1 + min(self.minOperations(n + 1), self.minOperations(n - 1))