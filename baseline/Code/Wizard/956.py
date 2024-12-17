from typing import List
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        if n % 2 == 0:
            return 10 ** (n // 2) - 1
        else:
            return 10 ** ((n + 1) // 2) - 1