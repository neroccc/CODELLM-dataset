from typing import List, Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        for k, v in count.items():
            if v % 2 == 1:
                ans += v - 1
        return ans