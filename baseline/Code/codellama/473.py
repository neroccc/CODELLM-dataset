from typing import List
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4
        matchsticks.sort(reverse=True)

        def dfs(matchsticks, start, target, visited):
            if target == 0:
                return True
            if start == len(matchsticks):
                return False
            if visited[start] or target < 0:
                return False
            visited[start] = True
            res = (dfs(matchsticks, start + 1, target - matchsticks[start], visited) or
                   dfs(matchsticks, start + 1, target, visited) or
                   dfs(matchsticks, start + 1, target, visited) or
                   dfs(matchsticks, start + 1, target, visited))
            visited[start] = False
            return res

        return dfs(matchsticks, 0, target, [0] * 4)
    

