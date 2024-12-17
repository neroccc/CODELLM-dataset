from typing import List
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    dist[node] += dist[neighbor] + 1
                    count[node] += count[neighbor]

        def dfs2(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    dist[neighbor] = (n - count[neighbor]) * dist[node] + (n - count[neighbor] - 1) * (n - count[neighbor] - 1)
                    answer[neighbor] = dist[node] + answer[neighbor]
                    dfs2(neighbor, node)

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        dist = [0] * n
        count = [1] * n
        answer = [0] * n

        dfs(0, -1)
        dfs2(0, -1)

        return answer