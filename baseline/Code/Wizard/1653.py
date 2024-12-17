from typing import List
class Solution:
    def minDeletions(self, s: str) -> int:
        n = len(s)
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        count.sort(reverse=True)
        balanced = 0
        for c in count:
            if c % 2 == 1:
                balanced += 1
            else:
                balanced -= 1

        return balanced