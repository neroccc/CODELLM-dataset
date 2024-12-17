from collections import defaultdict
from heapq import heappop, heappush
from typing import List
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        min_dist = [float('inf')] * n
        ways = [0] * n
        min_dist[0] = 0
        ways[0] = 1
        heap = [(0, 0)]

        while heap:
            d, node = heappop(heap)
            if d != min_dist[node]:
                continue
            for neigh, t in graph[node]:
                if d + t < min_dist[neigh]:
                    min_dist[neigh] = d + t
                    ways[neigh] = ways[node]
                    heappush(heap, (min_dist[neigh], neigh))
                elif d + t == min_dist[neigh]:
                    ways[neigh] = (ways[neigh] + ways[node]) % (10**9 + 7)

        return ways[-1]