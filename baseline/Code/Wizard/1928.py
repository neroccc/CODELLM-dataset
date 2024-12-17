from collections import defaultdict
from typing import List
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        graph = defaultdict(list)
        for x, y, time in edges:
            graph[x].append((y, time))
            graph[y].append((x, time))

        def dfs(city, time, visited, path, cost):
            if city == n - 1:
                return cost
            if time >= maxTime:
                return float('inf')
            visited.add(city)
            min_cost = float('inf')
            for neighbor, time_to_neighbor in graph[city]:
                if neighbor not in visited:
                    min_cost = min(min_cost, dfs(neighbor, time + time_to_neighbor, visited, path + [neighbor], cost + passingFees[neighbor]))
            visited.remove(city)
            return min_cost

        return dfs(0, 0, set(), [0], 0) if dfs(0, 0, set(), [0], 0) != float('inf') else -1