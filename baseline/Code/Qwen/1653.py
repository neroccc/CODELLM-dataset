from typing import List
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a_count = s.count('a')
        b_count = 0
        min_deletions = n - a_count

        for char in s:
            if char == 'a':
                a_count -= 1
            else:
                b_count += 1

            min_deletions = min(min_deletions, a_count + b_count)

        return min_deletions