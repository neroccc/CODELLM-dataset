from typing import List
class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        freq = [0] * 31
        for num in nums:
            freq[num] += 1
        dp = [0] * (1 << 10)
        dp[0] = 1
        for i in range(1, 31):
            if freq[i] == 0:
                continue
            g = []
            for j in range(10):
                if i % primes[j] == 0:
                    g.append(j)
            if len(g) > 0:
                dp2 = dp[:]
                for mask in range(1 << len(g)):
                    for j in range(len(g)):
                        if ((mask >> j) & 1) == 1:
                            dp2[mask] = (dp2[mask] + dp[mask ^ (1 << j)] * freq[i]) % MOD
                dp = dp2
        ans = sum(dp[mask] * freq[1] for mask in range(1 << 10)) % MOD
        return pow(2, freq[1], MOD) * ans % MOD