from typing import List
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for r in rods:
            ndp = dp.copy()
            for diff, height in dp.items():
                ndp[diff + r] = max(ndp.get(diff + r, 0), height)
                ndp[abs(diff - r)] = max(ndp.get(abs(diff - r), 0), height + min(diff, r))
            dp = ndp
        return dp[0]