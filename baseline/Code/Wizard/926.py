from typing import List
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        ones = [0] * n
        zeros = [0] * n

        for i in range(n):
            if s[i] == '0':
                zeros[i] = 0
                ones[i] = 0
            else:
                zeros[i] = zeros[i - 1] + 1
                ones[i] = ones[i - 1]

        for i in range(1, n):
            if s[i] == '1':
                ones[i] = min(ones[i - 1] + 1, zeros[i])
            else:
                zeros[i] = min(zeros[i - 1] + 1, ones[i])

        return min(ones[-1], zeros[-1])