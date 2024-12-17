import sys
from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        idx = [0] * len(primes)
        for i in range(1, n):
            ugly[i] = sys.maxsize
            for j in range(len(primes)):
                ugly[i] = min(ugly[i], primes[j] * ugly[idx[j]])
            for j in range(len(primes)):
                while ugly[i] % primes[j] == 0:
                    idx[j] += 1
                    ugly[i] //= primes[j]
        return ugly[-1]