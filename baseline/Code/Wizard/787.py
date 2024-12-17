from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        INF = float('inf')
        dp = [[INF] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        for k in range(1, k + 1):
            for u in range(n):
                for v in range(n):
                    for nei, w in graph[u]:
                        dp[u][v] = min(dp[u][v], dp[u][nei] + w)

        return dp[src][dst] if dp[src][dst] != INF else -1