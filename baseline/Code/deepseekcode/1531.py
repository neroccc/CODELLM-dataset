from typing import List
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(n, -1, -1):
            for j in range(k + 1):
                if i == n:
                    dp[i][j] = 0
                elif j == 0:
                    dp[i][j] = dp[i + 1][j]
                else:
                    same, diff = 0, 0
                    for p in range(i + 1, n + 1):
                        if s[i] == s[p - 1]:
                            same += 1
                        else:
                            diff += 1
                        if diff > j:
                            break
                        len = 1 + (same if same < 10 else (same if same < 100 else same))
                        delete = diff if same == 1 else (diff if same < 10 else (diff if same < 100 else diff))
                        dp[i][j] = min(dp[i][j], dp[p][j - delete] + len)

        return dp[0][k]