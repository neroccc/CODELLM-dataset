from typing import List
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        s = str(n)
        length = len(s)
        first = int(s[0])
        other_digits = int(s[1:])

        dp = [[0] * length for _ in range(length)]
        dp[0][0] = first > 1

        for i in range(1, length):
            dp[0][i] = dp[0][i - 1] * 10 + (first > 1)

        for i in range(1, length):
            dp[i][i] = dp[i - 1][i - 1] * 10 + (first > 1) * (10 ** i)
            for j in range(i + 1, length):
                dp[i][j] = dp[i - 1][j - 1] * 10 + dp[i][j - 1] + (first > 1) * (10 ** i)

        return dp[length - 1][length - 1] + (first == 1) * (other_digits + 1) + self.countDigitOne(other_digits)