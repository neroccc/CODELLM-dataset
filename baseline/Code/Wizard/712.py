from typing import List
class Solution:
    def minCharDeletions(self, s1: str, s2: str) -> int:
        freq1 = [0] * 26
        freq2 = [0] * 26

        for c in s1:
            freq1[ord(c) - ord('a')] += 1

        for c in s2:
            freq2[ord(c) - ord('a')] += 1

        freq = [0] * 26
        for i in range(26):
            freq[i] = max(freq1[i], freq2[i])

        return sum(i * (freq[i] - min(freq1[i], freq2[i])) for i in range(26))