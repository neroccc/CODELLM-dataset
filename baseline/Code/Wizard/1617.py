from typing import List
class Solution:
    def countSubtrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        def dfs(node, parent):
            subtree_sizes = [1] * n
            for neighbor in graph[node]:
                if neighbor != parent:
                    subtree_sizes[node] += dfs(neighbor, node)
            return subtree_sizes

        subtree_sizes = dfs(0, -1)
        result = [0] * (n - 1)

        for d in range(1, n):
            for i in range(n):
                for j in range(n):
                    if subtree_sizes[i] * subtree_sizes[j] == d:
                        result[d - 1] += 1

        return result