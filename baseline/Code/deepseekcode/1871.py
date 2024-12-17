from typing import List
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            for j in range(max(0, i - maxJump), max(0, i - minJump) + 1):
                if dp[j] and s[i] == '0':
                    dp[i] = 1
                    break
        return dp[-1] == 1