from typing import List
class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [0] * 32
        dp[0] = 1
        dp[1] = 2
        for i in range(2, 32):
            dp[i] = dp[i - 1] + dp[i - 2]

        ans = 0
        prev = 0
        for i in range(31, -1, -1):
            if n & (1 << i):
                ans += dp[i]
                if prev == 1:
                    ans -= 1
                    break
                prev = 1
            else:
                prev = 0
        return ans + 1