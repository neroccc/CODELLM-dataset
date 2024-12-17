from collections import defaultdict
from typing import List
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res = [0] * n
        visited = [0] * n

        def dfs(node):
            visited[node] = 1
            count = [0] * 26
            count[ord(labels[node]) - 97] = 1
            for nei in graph[node]:
                if visited[nei] == 0:
                    temp = dfs(nei)
                    if sum(temp) > sum(count):
                        count = temp
            res[node] = sum(count)
            return count

        dfs(0)
        return res