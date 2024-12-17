from typing import List
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s += s
        s = '0' + s + '0'
        ans = n
        for i in range(2 * n + 1):
            cnt = 0
            for j in range(n + 1):
                if s[i + j] != s[j]:
                    cnt += 1
            ans = min(ans, cnt, n - cnt)
        return ans