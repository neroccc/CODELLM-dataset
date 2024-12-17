from typing import List
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        graph = [[] for _ in range(n)]
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        dp = [[float('inf')] * n for _ in range(maxTime + 1)]
        dp[0][0] = passingFees[0]

        for time in range(1, maxTime + 1):
            for u in range(n):
                for v, t in graph[u]:
                    if time - t >= 0:
                        dp[time][v] = min(dp[time][v], dp[time - t][u] + passingFees[v])

        ans = min(dp[maxTime])
        return ans if ans != float('inf') else -1