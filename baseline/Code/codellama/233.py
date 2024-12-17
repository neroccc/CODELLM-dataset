from typing import List
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 1:
            return 1
        if n <= 9:
            return n
        if n <= 99:
            return 1 + n // 10 + n % 10
        if n <= 999:
            return 1 + n // 100 + n // 10 % 10 + n % 10
        if n <= 9999:
            return 1 + n // 1000 + n // 100 % 10 + n // 10 % 10 + n % 10
        if n <= 99999:
            return 1 + n // 10000 + n // 1000 % 10 + n // 100 % 10 + n // 10 % 10 + n % 10
        if n <= 999999:
            return 1 + n // 100000 + n // 10000 % 10 + n // 1000 % 10 + n // 100 % 10 + n // 10 % 10 + n % 10
        if n <= 9999999:
            return 1 + n // 1000000 + n // 100000 % 10 + n // 10000 % 10 + n // 1000 % 10 + n // 100 % 10 + n // 10 % 10 + n % 10
        if n <= 99999999:
            return 1 + n // 10000000 + n // 1000000 % 10 + n // 100000 % 10 + n // 10000 % 10 + n // 1000 % 10 + n // 10