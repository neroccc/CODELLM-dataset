from typing import List
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if n % 2 == 0:
            return self.minOperationsHelper(s, n // 2)
        else:
            return min(self.minOperationsHelper(s, n // 2), self.minOperationsHelper(s, (n // 2) + 1))

    def minOperationsHelper(self, s, k):
        if k == 0:
            return 0

        if k == 1:
            if s[0] == s[-1]:
                return 1
            else:
                return 0

        if s[0] == s[-1]:
            return self.minOperationsHelper(s[1:-1], k - 1)
        else:
            return 1 + self.minOperationsHelper(s[1:-1], k - 1)