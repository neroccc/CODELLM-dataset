from typing import List
class Solution:
    def minPrinterTurns(self, s: str) -> int:
        n = len(s)
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        even_count = 0
        odd_count = 0
        for c in count:
            if c % 2 == 0:
                even_count += c // 2
            else:
                even_count += c // 2
                odd_count += 1

        return min(even_count, odd_count)