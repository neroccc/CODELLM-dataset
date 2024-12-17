import heapq
from typing import List
class Solution:
    def shortestDistance(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float("inf")] * n
        dist[0] = 0
        seen = [False] * n
        heap = [(0, 0)]
        while heap:
            d, node = heapq.heappop(heap)
            if seen[node]:
                continue
            seen[node] = True
            for nei, w in graph[node]:
                dist[nei] = min(dist[nei], d + w)
                heapq.heappush(heap, (dist[nei], nei))

        return sum(dist) % (10 ** 9 + 7)