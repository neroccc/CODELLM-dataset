from typing import List
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True

        for i in range(1, n):
            j = i - 1
            while j >= 0 and s[j] == '0' and (i - j) <= maxJump:
                dp[i] = dp[j] or dp[i]
                j -= 1
            if s[i] == '0':
                dp[i] = dp[i] or dp[i - minJump]

        return dp[-1]