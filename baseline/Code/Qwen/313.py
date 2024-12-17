from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1] * n
        m = len(primes)
        index = [0] * m
        multiples = [1] * m

        for i in range(1, n):
            min_val = float('inf')
            for j in range(m):
                min_val = min(min_val, dp[index[j]] * primes[j])
            dp[i] = min_val

            for j in range(m):
                if dp[index[j]] * primes[j] == min_val:
                    index[j] += 1

        return dp[-1]