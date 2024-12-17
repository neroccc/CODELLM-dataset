from typing import List
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        bCount = 0
        for i in range(n):
            if s[i] == 'b':
                bCount += 1
            else:
                dp[i] = min(bCount, dp[i-1] + 1) if i > 0 else bCount
        return dp[-1]