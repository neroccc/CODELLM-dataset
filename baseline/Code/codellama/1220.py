from typing import List
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        for i in range(1, n):
            for j in range(4):
                dp[j] = dp[j] * (i + 1) + dp[j + 1]
        return dp[0] % (10 ** 9 + 7)