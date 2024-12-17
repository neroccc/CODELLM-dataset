from typing import List
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        ones = s.count('1')
        zeros = 0
        ans = n - ones
        for i in range(n):
            if s[i] == '1':
                ones -= 1
            else:
                zeros += 1
            ans = min(ans, zeros + ones)
        return ans