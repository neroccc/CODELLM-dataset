from typing import List
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dp = [float('inf')] * (maxTime + 1)
        dp[0] = passingFees[0]

        heap = [(passingFees[0], 0, 0)]
        while heap:
            cost, time, node = heapq.heappop(heap)
            if node == len(passingFees) - 1:
                return cost
            if time > maxTime:
                continue
            for nei, nei_time in graph[node]:
                new_cost = cost + passingFees[nei]
                new_time = time + nei_time
                if new_time <= maxTime and new_cost < dp[new_time]:
                    dp[new_time] = new_cost
                    heapq.heappush(heap, (new_cost