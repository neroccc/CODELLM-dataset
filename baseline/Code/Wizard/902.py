from typing import List
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        if n == 2:
            return 91

        dp = [1, 10, 91]
        for i in range(3, n + 1):
            count = 0
            for j in range(9):
                count += dp[i - 1]
                if j > 0:
                    count -= (9 - j) * dp[i - 1]
            dp.append(count)

        return dp[n]