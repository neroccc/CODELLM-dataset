from typing import List
class Solution:
    def minimumDistance(self, word: str) -> int:
        def cost(pos1: int, pos2: int) -> int:
            x1, y1 = divmod(pos1, 6)
            x2, y2 = divmod(pos2, 6)
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(word)
        dp, dp2, dp3 = [0] * 26, [0] * 26, [0] * 26
        for i in range(n - 1, -1, -1):
            pos = ord(word[i]) - 65
            for j in range(26):
                dp2[j] = min(cost(pos, j) + dp[j], cost(pos, pos) + dp3[j])
            dp, dp3, dp2 = dp2, dp, [0] * 26
        return min(dp)