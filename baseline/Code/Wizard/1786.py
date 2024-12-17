from collections import defaultdict
from typing import List
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w

        distance = [0] * (n + 1)
        distance[n] = float('inf')

        def dfs(node, last_node):
            nonlocal distance
            for neighbor, weight in graph[node].items():
                if neighbor != last_node:
                    dfs(neighbor, node)
                    distance[node] = min(distance[node], distance[neighbor] + weight)

        dfs(1, -1)

        def countPaths(node, last_node):
            nonlocal distance
            count = 0
            for neighbor, weight in graph[node].items():
                if neighbor != last_node and distance[neighbor] > distance[node]:
                    count += countPaths(neighbor, node)
            return count

        return countPaths(1, -1) % (10**9 + 7)