from typing import List
class Solution:
    def countBinarySubstrings(self, n: int) -> int:
        s = bin(n)[2:]
        n = len(s)
        count = 0
        prev = 0
        curr = 1

        for i in range(1, n):
            if s[i] == '1':
                count += min(prev, curr)
                prev = curr
                curr = 1
            else:
                curr += 1

        return count + n