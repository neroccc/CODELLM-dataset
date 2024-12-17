from typing import List
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False

        dp = [False] * (n2 + 1)
        dp[0] = True

        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i > 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
                if j > 0:
                    dp[j] = dp[j] or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[-1]