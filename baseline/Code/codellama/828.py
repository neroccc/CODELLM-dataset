from typing import List
class Solution:
    def countUniqueChars(self, s: str) -> int:
        unique = set(s)
        return sum(len(unique) for unique in unique)

    def sumOfUniqueChars(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    ans += self.countUniqueChars(s[i : j + 1])
        return ans