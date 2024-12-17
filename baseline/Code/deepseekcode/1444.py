from functools import lru_cache
from typing import List
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        rows, cols = len(pizza), len(pizza[0])
        prefix = [[0]*(cols+1) for _ in range(rows+1)]
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                prefix[r][c] = prefix[r+1][c] + prefix[r][c+1] - prefix[r+1][c+1] + (pizza[r][c] == 'A')
        @lru_cache(None)
        def dp(r, c, k):
            if k == 0: return int(prefix[r][c] > 0)
            ans = sum(dp(i, c, k-1) + dp(r, j, k-1) for i in range(r+1, rows) for j in range(c, cols) if prefix[r][c] - prefix[i][c] - prefix[r][j] + prefix[i][j] > 0) % MOD
            return ans
        return dp(0, 0, k-1)