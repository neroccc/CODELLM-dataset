from typing import List
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        dp = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        visited = set()

        def dfs(node, turn, move):
            if (node, turn, move) in visited:
                return dp[node][turn][move]

            visited.add((node, turn, move))

            if node == 0:
                if turn == 1:
                    dp[node][turn][move] = 2
                else:
                    dp[node][turn][move] = 1
                return dp[node][turn][move]

            if move == 2:
                dp[node][turn][move] = 0
                return dp[node][turn][move]

            if move == 1:
                dp[node][turn][move] = 2
                for next_node in graph[node]:
                    if dfs(next_node, 1 - turn, 2) == 2:
                        dp[node][turn][move] = 1
                        break
            else:
                dp[node][turn][move] = 1
                for next_node in graph[node]:
                    if dfs(next_node, 1 - turn, 1) == 1:
                        dp[node][turn][move] = 2
                        break

            return dp[node][turn][move]

        return dfs(1, 0, 1)