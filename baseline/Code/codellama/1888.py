from typing import List
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(1, n):
            if s[i] == s[i - 1]:
                ans += 1
        return ans