from typing import List
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        adj_list = [[] for _ in range(n)]
        time = [float('inf')] * n
        time[0] = 0
        time[n - 1] = 0

        for u, v, t in roads:
            adj_list[u].append((v, t))
            adj_list[v].append((u, t))

        def dfs(node, prev):
            for neighbor, t in adj_list[node]:
                if neighbor != prev:
                    if time[node] + t < time[neighbor]:
                        time[neighbor] = time[node] + t
                        dfs(neighbor, node)

        dfs(0, -1)
        dfs(n - 1, -1)

        dp = [1] * n
        for i in range(n - 2, -1, -1):
            for neighbor, t in adj_list[i]:
                if time[i] + t == time[neighbor]:
                    dp[i] = (dp[i] + dp[neighbor]) % MOD

        return dp[0]