import heapq
from typing import List
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        adj = [[] for _ in range(n)]
        for u, v, t in roads:
            adj[u].append((v, t))
            adj[v].append((u, t))

        dist = [float('inf')] * n
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1

        pq = [(0, 0)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, t in adj[u]:
                if d + t < dist[v]:
                    dist[v] = d + t
                    ways[v] = ways[u]
                    heapq.heappush(pq, (dist[v], v))
                elif d + t == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1]