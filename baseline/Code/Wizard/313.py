from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        idx = [0] * len(primes)
        val = [1] * len(primes)

        for i in range(n - 1):
            next_ugly = float('inf')
            next_prime = 0

            for j in range(len(primes)):
                while val[j] * primes[j] <= ugly[-1]:
                    val[j] *= primes[j]
                    idx[j] += 1

            for j in range(len(primes)):
                if val[j] * primes[j] < next_ugly:
                    next_ugly = val[j] * primes[j]
                    next_prime = primes[j]

            ugly.append(next_ugly)

        return ugly[-1]