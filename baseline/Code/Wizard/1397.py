from typing import List
class Solution:
    def countGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        s1_ord = ord(s1[0])
        s2_ord = ord(s2[-1])
        evil_set = set(evil)

        def count_good(start, end, evil_set):
            count = 0
            for i in range(start, end + 1):
                for j in range(ord('a'), ord('z') + 1):
                    if chr(i) == chr(j):
                        count += 1
                        if i == start and chr(j) in evil_set:
                            count -= 1
                        if i == end and chr(j) in evil_set:
                            count -= 1
            return count

        return count_good(s1_ord, s2_ord, evil_set) * (n - 1) % MOD