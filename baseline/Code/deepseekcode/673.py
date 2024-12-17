from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, ans = float('-inf'), 0
        for pair in sorted(pairs, key=lambda x: x[1]):
            if cur < pair[0]:
                cur = pair[1]
                ans += 1
        return ans