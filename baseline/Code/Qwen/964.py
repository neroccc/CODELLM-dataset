from typing import List
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        def dfs(target):
            if target == 1:
                return 0
            if target % x == 0:
                return target // x - 1
            if target % x == 1:
                return target // x
            return min(dfs(target // x) + 1 + target % x, dfs(target // x + 1) + 1 + x - target % x)

        return dfs(target)