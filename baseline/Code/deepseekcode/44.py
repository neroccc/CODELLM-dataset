from typing import List
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s, len_p = len(s), len(p)
        dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]
        
        dp[-1][-1] = True
        for i in range(len_p - 1, -1, -1):
            if p[i] == '*':
                dp[-1][i] = dp[-1][i + 1]
                
        for i in range(len_s - 1, -1, -1):
            for j in range(len_p - 1, -1, -1):
                if p[j] in {s[i], '?'}:
                    dp[i][j] = dp[i + 1][j + 1]
                elif p[j] == '*':
                    dp[i][j] = dp[i + 1][j] or dp[i][j + 1]
        
        return dp[0][0]