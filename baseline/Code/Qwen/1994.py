from typing import List
class Solution:
    def countDistinct(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        n = len(nums)
        dp = [1] + [0] * n
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] += dp[j]
                    dp[i] %= 10**9 + 7
        return sum(dp) % (10**9 + 7)