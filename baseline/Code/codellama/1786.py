from collections import defaultdict
from typing import List
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        mod = 1000000007
        dp = [[0] * n for _ in range(1 << n)]
        dp[1 << n - 1][0] = 1
        for state in range(1 << n):
            for i in range(n):
                if state >> i & 1:
                    for j, w in graph[i + 1]:
                        if state >> j & 1:
                            dp[state][i] += dp[state - (1 << j)][j] * w
                            dp[state][i] %= mod
        return sum(dp[-1]) % mod
