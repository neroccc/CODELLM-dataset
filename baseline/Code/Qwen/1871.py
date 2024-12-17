from typing import List
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1':
            return False

        dp = [False] * n
        dp[0] = True
        for i in range(1, n):
            if i >= minJump and dp[i - minJump]:
                dp[i] = True
            if i > maxJump and dp[i - maxJump - 1]:
                dp[i] = True

        return dp[-1]