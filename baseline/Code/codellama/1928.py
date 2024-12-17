from typing import List
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        dist = [float('inf')] * n
        dist[0] = 0
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        pq = [(0, 0)]
        while pq:
            time, node = heapq.heappop(pq)
            if time > maxTime:
                continue
            if time > dist[node]:
                continue
            for nei, cost in graph[node]:
                if time + cost < dist[nei]:
                    dist[nei] = time + cost
                    heapq.heappush(pq