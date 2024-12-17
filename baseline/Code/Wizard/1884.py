from typing import List
class Solution:
    def superEggDrop(self, n: int, k: int) -> int:
        memo = {}

        def dp(eggs: int, floors: int) -> int:
            if (eggs, floors) in memo:
                return memo[(eggs, floors)]

            if eggs == 1:
                return floors
            if floors == 0:
                return 0
            if floors == 1:
                return 1

            ans = float('inf')
            for i in range(1, floors + 1):
                ans = min(ans, max(dp(eggs - 1, i - 1), dp(eggs, floors - i)) + 1)

            memo[(eggs, floors)] = ans
            return ans

        return dp(k, n)