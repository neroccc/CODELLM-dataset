from typing import List
class Solution:
    def countGoodSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        def get_factors(num):
            factors = set()
            for prime in primes:
                if prime > num:
                    break
                while num % prime == 0:
                    factors.add(prime)
                    num //= prime
            return factors

        def count_subsets(nums):
            dp = [0] * (len(nums) + 1)
            dp[0] = 1
            for num in nums:
                new_dp = [0] * (len(nums) + 1)
                factors = get_factors(num)
                for i in range(len(nums) + 1):
                    for factor in factors:
                        new_dp[i + 1] += dp[i]
                        new_dp[i + 1] %= MOD
                dp = new_dp
            return dp[-1]

       