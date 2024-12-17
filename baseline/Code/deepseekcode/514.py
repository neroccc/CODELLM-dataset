from typing import List
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m, n = len(ring), len(key)
        pos = [[] for _ in range(26)]
        for i in range(m):
            pos[ord(ring[i]) - ord('a')].append(i)
        dp = [0] * m
        for i in range(n):
            dp2 = [0] * m
            for j in pos[ord(key[i]) - ord('a')]:
                if i == 0:
                    dp2[j] = min(j, m - j) + 1
                else:
                    for k in pos[ord(key[i - 1]) - ord('a')]:
                        dp2[j] = min(dp2[j], dp[k] + min(abs(j - k), m - abs(j - k)) + 1)
            dp = dp2
        return min(dp)