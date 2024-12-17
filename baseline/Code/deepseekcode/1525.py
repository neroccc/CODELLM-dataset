from typing import List
class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        prefix_count = [0] * n
        suffix_count = [0] * n
        prefix_set = set()
        suffix_set = set()
        count = 0

        for i in range(n):
            prefix_set.add(s[i])
            prefix_count[i] = len(prefix_set)
            suffix_set.add(s[n - i - 1])
            suffix_count[n - i - 1] = len(suffix_set)

        for i in range(n - 1):
            if prefix_count[i] == suffix_count[i + 1]:
                count += 1

        return count