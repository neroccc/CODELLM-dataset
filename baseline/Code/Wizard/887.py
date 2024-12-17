from typing import List
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = {}

        def dp(eggs, floors):
            if (eggs, floors) in memo:
                return memo[(eggs, floors)]
            if eggs == 1:
                return floors
            if floors == 0:
                return 0
            if floors == 1:
                return 1

            memo[(eggs, floors)] = float('inf')
            for i in range(1, floors + 1):
                memo[(eggs, floors)] = min(
                    memo[(eggs, floors), memo[eggs - 1, i - 1] + dp(eggs, floors - i) + 1],
                    memo[eggs, floors]
                )
            return memo[(eggs, floors)]

        return dp(k, n)