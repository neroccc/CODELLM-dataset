from collections import defaultdict
from math import comb
from typing import List
class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(prevRoom)
        graph = defaultdict(list)
        for i in range(1, n):
            graph[prevRoom[i]].append(i)

        size = [0]*n
        def dfs(x):
            size[x] = 1
            for y in graph[x]:
                dfs(y)
                size[x] += size[y]

        dfs(0)

        f = [0]*n
        f[0] = 1
        for x in range(1, n):
            f[x] = f[size[x]-1] * comb(sum(f[:x]), size[x]-1) % MOD

        return sum(f) % MOD