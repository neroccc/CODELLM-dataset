from typing import List
class Solution:
    def countGoodSplits(self, s: str) -> int:
        n = len(s)
        count = 0
        freq = [0] * 26
        for i in range(n):
            freq[ord(s[i]) - ord('a')] += 1

        for i in range(n - 1):
            for j in range(i + 1, n):
                if freq[ord(s[i]) - ord('a')] == 1:
                    count += 1
                freq[ord(s[i]) - ord('a')] -= 1
                freq[ord(s[j]) - ord('a')] += 1

        return count