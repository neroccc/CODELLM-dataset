from typing import List
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4:
            return False
        side_length = total_length // 4
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def dfs(index):
            if index == len(matchsticks):
                return all(side == side_length for side in sides)
            for i in range(4):
                if sides[i] + matchsticks[index] <= side_length:
                    sides[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
                if not sides[i]:
                    break
            return False

        return dfs(0)