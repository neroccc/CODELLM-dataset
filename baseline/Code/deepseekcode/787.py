import heapq
from collections import defaultdict
from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        best = [None] * n
        work = [(0, src, k + 1)]
        while work:
            cost, node, k = heapq.heappop(work)
            if node == dst:
                return cost
            if k < 0:
                continue
            if best[node] is None or best[node] > cost:
                best[node] = cost
            for nei, nei_cost in graph[node]:
                if best[nei] is None or best[nei] > cost + nei_cost:
                    heapq.heappush(work, (cost + nei_cost, nei, k - 1))
        return -1