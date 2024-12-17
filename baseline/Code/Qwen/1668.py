from typing import List
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        ans = 0

        for i in range(n - m + 1):
            j = 0
            while j < m and sequence[i + j] == word[j]:
                j += 1
            ans = max(ans, j // m)

        return ans