from typing import List
class Solution:
    def countUniqueChars(self, s: str) -> int:
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        return sum(count.values())

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                ans += self.countUniqueChars(s[i:j+1])
        return ans