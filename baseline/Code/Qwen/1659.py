from functools import cache
from typing import List
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        @cache
        def dp(i, j, introverts, extroverts):
            if i == m or j == n:
                return 0
            if introverts == 0 and extroverts == 0:
                return 0
            ans = dp(i, j + 1, introverts, extroverts)
            if introverts > 0:
                ans = max(ans, dp(i, j + 1, introverts - 1, extroverts) + 120 - 30 * (j > 0) - 30 * (i > 0))
            if extroverts > 0:
                ans = max(ans, dp(i, j + 1, introverts, extroverts - 1) + 40 + 20 * (j > 0) + 20 * (i > 0))
            return ans

        return dp(0, 0, introvertsCount, extrovertsCount)