from typing import List
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        n = len(s1)
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]
        for diff in range(2, n + 1):
            for i in range(n - diff + 1):
                for j in range(n - diff + 1):
                    for k in range(1, diff):
                        if dp[i][j][k] and dp[i + k][j + k][diff - k]:
                            dp[i][j][diff] = True
                            break
                        if dp[i][j + diff - k][k] and dp[i + k][j][diff - k]:
                            dp[i][j][diff] = True
                            break
        return dp[0][0][n]