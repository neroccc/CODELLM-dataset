from typing import List
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        m, k = len(digits), len(s)
        dp = [[0] * (k + 1) for _ in range(2)]
        dp[0][0] = 1

        for i in range(1, k + 1):
            for j in range(m):
                if s[i - 1] == digits[j]:
                    dp[0][i] += dp[0][i - 1]
                if s[i - 1] > digits[j]:
                    dp[1][i] += dp[1][i - 1]
                else:
                    break

        return dp[0][k] + dp[1][k] * m + sum(dp[0][i] for i in range(1, k))