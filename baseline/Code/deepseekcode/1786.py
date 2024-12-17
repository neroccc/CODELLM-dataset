import collections
import heapq
from typing import List
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        heap = [(0, n)]
        while heap:
            d, node = heapq.heappop(heap)
            if d != dist[node]:
                continue
            for neighbor, w in graph[node]:
                if d + w < dist[neighbor]:
                    dist[neighbor] = d + w
                    heapq.heappush(heap, (dist[neighbor], neighbor))

        dp = [0] * (n + 1)
        dp[n] = 1
        heap = [(-dist[1], 1)]
        while heap:
            d, node = heapq.heappop(heap)
            if -d != dist[node]:
                continue
            for neighbor, _ in graph[node]:
                if dist[neighbor] > dist[node]:
                    dp[node] += dp[neighbor]
                    dp[node] %= (10**9 + 7)
                    heapq.heappush(heap, (-dist[node], node))

        return dp[1]