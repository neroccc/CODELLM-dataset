from typing import List
class Solution:
    def numSub(self, binary: str) -> int:
        MOD = 10**9 + 7
        count = 0
        ans = 0

        for c in binary:
            if c == '1':
                count += 1
                ans = (ans + count) % MOD
            else:
                count = 0

        return ans