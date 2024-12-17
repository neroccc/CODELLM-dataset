from functools import lru_cache
from typing import List, Tuple


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        remainders = [0] * batchSize
        for group in groups:
            remainders[group % batchSize] += 1

        @lru_cache(None)
        def dp(remainder: int, cnt: Tuple[int]) -> int:
            ans = remainders[0] if remainder == 0 else -1
            for x in range(1, batchSize):
                if cnt[x] > 0:
                    next_cnt = list(cnt)
                    next_cnt[x] -= 1
                    next_remainder = (remainder - x) % batchSize
                    ans = max(ans, dp(next_remainder, tuple(next_cnt)) + (remainder == 0))
            return ans

        return dp(0, tuple(remainders[1:]))