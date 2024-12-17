from typing import List
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        evil_len = len(evil)
        evil_suffixes = [evil[i:] for i in range(evil_len)]
        evil_suffixes.sort()

        def dp(i, j, k, is_prefix, is_suffix):
            if k == evil_len:
                return 0
            if i == n and j == n:
                return 1
            if i == n:
                return dp(i, j + 1, k, is_prefix, is_suffix)
            if j == n:
                return dp(i + 1, j, k, is_prefix, is_suffix)

            if is_prefix and is_suffix:
                return (dp(i + 1, j, k, is_prefix, is_suffix) + dp(i, j + 1, k, is_prefix, is_suffix)) % MOD

            if is_prefix:
                return dp(i + 1, j, k, is_prefix, is_suffix)

            if is_suffix:
                return dp(i, j + 1, k, is_prefix, is_suffix)

            if s1[i] == s2[j]:
                return (dp(i + 1, j, k, is_prefix, is_suffix) + dp(i, j + 1, k, is_prefix, is_suffix)) % MOD

            if s1[i] < s2[j]:
                return dp(i + 1, j, k, is_prefix, is_suffix)

            if s1[i] > s2[j]:
                return dp(i, j + 1, k, is_prefix, is_suffix)

            if s1[i] == s2[j]:
                