from typing import List
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)
        dp = [[float('inf')] * n for _ in range(m)]
        pos = {c: [] for c in key}
        for i, c in enumerate(ring):
            pos[c].append(i)

        for i, c in enumerate(key):
            for j in pos[c]:
                if i == 0:
                    dp[i][j] = min(dp[i][j], j, n - j)
                else:
                    for k in pos[key[i - 1]]:
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + min(abs(j - k), n - abs(j - k)))

        return min(dp[-1]) + m