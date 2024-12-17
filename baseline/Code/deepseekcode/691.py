import functools
from collections import Counter
from typing import List
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        @functools.lru_cache(None)
        def dp(t: str) -> int:
            if not t:
                return 0
            res = float('inf')
            t_counter = Counter(t)
            for s in stickers:
                if s[0] not in t_counter:
                    continue
                s_counter = Counter(s)
                next_t = ''
                for c in t:
                    if s_counter[c] > 0:
                        s_counter[c] -= 1
                    else:
                        next_t += c
                res = min(res, dp(next_t) + 1)
            return res

        ans = dp(target)
        return -1 if ans == float('inf') else ans