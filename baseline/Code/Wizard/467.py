from typing import List
class Solution:
    def unique_substrings(self, s: str) -> int:
        base = "abcdefghijklmnopqrstuvwxyz" * 2
        base_set = set(base)
        count = 0

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in base_set:
                    count += 1

        return count