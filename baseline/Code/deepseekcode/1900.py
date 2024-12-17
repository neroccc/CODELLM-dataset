from typing import List
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        def helper(n, firstPlayer, secondPlayer, dp):
            if n == 1:
                return 1
            if firstPlayer > n // 2:
                firstPlayer = n - firstPlayer + 1
            if secondPlayer > n // 2:
                secondPlayer = n - secondPlayer + 1
            if (n, firstPlayer, secondPlayer) in dp:
                return dp[(n, firstPlayer, secondPlayer)]
            if firstPlayer == secondPlayer or secondPlayer == n - firstPlayer + 1:
                dp[(n, firstPlayer, secondPlayer)] = helper(n - 1, firstPlayer, secondPlayer, dp) + 1
            else:
                dp[(n, firstPlayer, secondPlayer)] = min(helper(n - 1, firstPlayer, secondPlayer, dp), helper(n - 1, firstPlayer, n - secondPlayer + 1, dp), helper(n - 1, n - firstPlayer + 1, secondPlayer, dp)) + 1
            return dp[(n, firstPlayer, secondPlayer)]

        return [helper(n, firstPlayer, secondPlayer, {}), helper(n, min(firstPlayer, n - firstPlayer + 1), max(firstPlayer, n - firstPlayer + 1), {