import heapq
from typing import List
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        dist = [float("inf")] * (n + 1)
        dist[n] = 0
        pq = [(0, n)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        dp = [0] * (n + 1)
        dp[n] = 1
        pq = [(dist[n], n)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                if dist[v] < dist[u]:
                    dp[v] = (dp[v] + dp[u]) % (10**9 + 7)
                    heapq.heappush(pq, (dist[v], v))

        return dp[1]