from typing import List
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        dp = [[[0] * n for _ in range(n)] for _ in range(2 * n)]

        def dfs(turn, mouse, cat):
            if turn == 0 and mouse == 0:
                return 1
            if turn == 1 and cat == 0:
                return 2
            if dp[turn][mouse][cat] != 0:
                return dp[turn][mouse][cat]

            if turn == 0:
                for next_mouse in graph[mouse]:
                    if next_mouse == cat:
                        continue
                    if dfs(1, next_mouse, cat) == 2:
                        dp[turn][mouse][cat] = 1
                        return 1
            else:
                for next_cat in graph[cat]:
                    if next_cat == 0:
                        continue
                    if dfs(0, mouse, next_cat) == 1:
                        dp[turn][mouse][cat] = 2
                        return 2

            dp[turn][mouse][cat] = 0
            return 0

        return dfs(0, 1, 2)