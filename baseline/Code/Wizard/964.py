from typing import List
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        if target == x:
            return 1
        if target % x == 0:
            return (target // x) + 1
        if target % x == 1:
            return (target // x) + 2
        if target % x == x - 1:
            return (target // x) + 2
        if target % x > x // 2:
            return (target // x) + 3
        else:
            return (target // x) + 2