from typing import List
class Solution:
    def numUniqueOccurrences(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return len(set(d.values()))
