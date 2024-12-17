from typing import List
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        a, b, c = [0]*3, [0]*3, [0]*3
        for num in nums:
            if num == 0:
                a[0] = (2*a[0] + 1) % mod
            elif num == 1:
                b[0] = (2*b[0] + a[0]) % mod
            else:
                c[0] = (2*c[0] + b[0]) % mod
            a[1], b[1], c[1] = a[0], b[0], c[0]
            a[2], b[2], c[2] = a[1], b[1], c[1]
        return c[2]