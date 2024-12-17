from typing import List
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for x in rods:
            dp = {a + x: max(b, dp.get(a, 0)) for a, b in dp.items()}
            dp = {a: max(b, dp.get(a - x, 0)) for a, b in dp.items()}
        return dp.get(0, 0)