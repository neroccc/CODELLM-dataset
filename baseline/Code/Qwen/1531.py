from typing import List
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            count = 0
            for j in range(i):
                if s[j] == s[i - 1]:
                    count += 1
                else:
                    count = 1
                for del_count in range(k + 1):
                    if del_count >= count:
                        dp[i][del_count] = min(dp[i][del_count], dp[j][del_count - count] + 1)
                    else:
                        dp[i][del_count] = min(dp[i][del_count], dp[j][del_count])

        return dp[n][k]