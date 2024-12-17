from typing import List
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        def helper(n):
            if n == 0:
                return 1
            if n == 1:
                return 2
            if n == 2:
                return 5
            if n == 3:
                return 13

            prev_ways = helper(n - 1)
            ways = 3 * prev_ways
            ways += 2 * (helper(n - 2) + helper(n - 3))
            return ways % MOD

        return helper(n) - 1