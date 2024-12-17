from typing import List
class Solution:
    def canReachEnd(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            for j in range(max(i - maxJump, 0), min(i + minJump, n - 1) + 1):
                if s[j] == '0' and dp[j]:
                    dp[i + 1] = True

        return dp[-1]