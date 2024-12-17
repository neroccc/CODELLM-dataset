from typing import List
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        s_hash = [0] * 26
        t_hash = [0] * 26
        count = 0

        for i in range(n):
            s_hash[ord(s[i]) - ord('a')] += 1

        for i in range(m):
            t_hash[ord(t[i]) - ord('a')] += 1

        for i in range(26):
            count += (s_hash[i] + t_hash[i]) // 2

        return count * (count - 1) // 2