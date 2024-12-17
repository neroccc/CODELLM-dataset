from typing import List
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks or sum(matchsticks) % 4 != 0:
            return False

        target = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)

        def dfs(index, sides):
            if index == len(matchsticks):
                return all(side == target for side in sides)

            for i in range(4):
                if sides[i] + matchsticks[index] <= target:
                    sides[i] += matchsticks[index]
                    if dfs(index + 1, sides):
                        return True
                    sides[i] -= matchsticks[index]

            return False

        return dfs(0, [0] * 4)