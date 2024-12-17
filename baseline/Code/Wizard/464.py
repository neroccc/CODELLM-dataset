from typing import List
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal > (1 + maxChoosableInteger) * maxChoosableInteger // 2:
            return False

        def dfs(choices, target, visited):
            if target <= 0:
                return False

            if target in visited[0]:
                return visited[0][target]

            for i in range(1, maxChoosableInteger + 1):
                if i in choices:
                    if not dfs(choices - {i}, target - i, visited):
                        visited[0][target] = True
                        return True

            visited[0][target] = False
            return False

        return dfs(set(range(1, maxChoosableInteger + 1)), desiredTotal, [{}, {}])