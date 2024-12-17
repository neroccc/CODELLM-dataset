from typing import List
class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        i, j, k = 0, n - 1, 0
        left, right = "", ""

        while i <= j:
            left, right = left + text[i], text[j] + right
            if left == right[::-1]:
                k += 2
                left, right = "", ""
            i += 1
            j -= 1

        if n - k == n:
            return n
        else:
            return k + 1