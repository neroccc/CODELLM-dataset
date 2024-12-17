from typing import List
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % mod

        inv = [1] * (n + 1)
        inv[n] = pow(fact[n], mod - 2, mod)
        for i in range(n - 1, -1, -1):
            inv[i] = inv[i + 1] * (i + 1) % mod

        def comb(n, k):
            return fact[n] * inv[k] % mod * inv[n - k] % mod

        def dfs(nums):
            if not nums:
                return 1
            root, *left, *right = sorted((x, i) for i, x in enumerate(nums))
            l = len(left)
            return comb(n - 1, l) * dfs(left) % mod * dfs(right) % mod

        return (dfs(nums) - 1) % mod