from functools import lru_cache
from typing import List
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        prefix = [0] * (len(stones) + 1)
        for i in range(len(stones)):
            prefix[i + 1] = prefix[i] + stones[i]

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            return max(prefix[j + 1] - prefix[i] - dp(i, j - 1), prefix[j] - prefix[i] - dp(i + 1, j))

        return dp(0, len(stones) - 1)