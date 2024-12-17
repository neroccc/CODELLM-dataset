from typing import List
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10

        dp = [1] * 10
        dp[1] = 9
        for i in range(2, n + 1):
            dp[i] = 9 * dp[i - 1] * (10 - i)

        return sum(dp) + 10 - 1