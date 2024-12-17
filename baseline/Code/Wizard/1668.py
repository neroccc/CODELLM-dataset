from typing import List
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        for k in range(n, 0, -1):
            if sequence[:m] == word * k:
                return k
        return 0