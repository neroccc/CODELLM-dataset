from typing import List
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            for i in range(n):
                if (mask >> i) & 1 == 0:
                    break
            else:
                for sticker in stickers:
                    new_mask = mask
                    for c in sticker:
                        for j in range(n):
                            if (new_mask >> j) & 1 == 0 and target[j] == c:
                                new_mask |= 1 << j
                                break
                    dp[new_mask] = min(dp[new_mask], dp[mask] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1