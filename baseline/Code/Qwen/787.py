from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))

        min_cost = [float('inf')] * n
        min_cost[src] = 0

        for _ in range(k + 1):
            new_min_cost = min_cost[:]
            for u in range(n):
                for v, w in graph[u]:
                    new_min_cost[v] = min(new_min_cost[v], min_cost[u] + w)
            min_cost = new_min_cost

        return min_cost[dst] if min_cost[dst] < float('inf') else -1