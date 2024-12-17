from typing import List
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        dp = [[float("inf")] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(n + 1):
            for j in range(n + 1):
                if dp[i][j] > dp[i][j - 1]:
                    dp[i][j] = dp[i][j - 1]

                if i < n and target[i] == target[j]:
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + 1)

                for sticker in stickers:
                    k = 0
                    while k < len(sticker) and j + k < n and sticker[k] == target[j + k]:
                        k += 1

                    if k > 0:
                        dp[i + k][j + k] = min(dp[i + k][j + k], dp[i][j] + 1)

        return dp[n][n] if dp[n][n] != float("inf") else -1