from typing import List
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        dp = [[-1] * n for _ in range(n)]
        return self.dfs(graph, dp, 1, 2, 0)
    
    def dfs(self, graph, dp, mouse, cat, hole):
        if dp[mouse - 1][cat - 1] != -1:
            return dp[mouse - 1][cat - 1]
        if mouse == hole:
            dp[mouse - 1][cat - 1] = 1
            return 1
        if cat == hole:
            dp[mouse - 1][cat - 1] = 2
            return 2
        for node in graph[mouse - 1]:
            if node == 0:
                continue
            if self.dfs(graph, dp, node, cat, hole) == 1:
                dp[mouse - 1][cat - 1] = 1
                return 1
        dp[mouse - 1][cat - 1] = 0
        return 0