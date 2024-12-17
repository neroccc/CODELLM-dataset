from collections import defaultdict
from typing import List
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(node, parent, visited):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor != parent and neighbor not in visited:
                    dfs(neighbor, node, visited)

        def bfs(node):
            visited = set()
            queue = [(node, 0)]
            visited.add(node)
            max_dist = 0
            while queue:
                node, dist = queue.pop(0)
                max_dist = max(max_dist, dist)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))
            return max_dist

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = [0] * (n - 1)
        for mask in range(1, 1 << n):
            visited = set()
            for i in range(n):
                if mask & (1 << i):
                    dfs(i + 1, -1, visited)
                    break
            if len(visited) == n:
                dist = bfs(visited.pop())
                if dist > 0:
                    ans[dist - 1] += 1

        return ans