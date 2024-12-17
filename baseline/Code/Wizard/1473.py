from typing import List
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        def dfs(house, color, target):
            if house == m:
                return 0 if target == 0 else float('inf')
            if dp[house][color]:
                return dp[house][color]
            if houses[house] != 0:
                dp[house][color] = cost[house][houses[house] - 1] if color == houses[house] else float('inf')
                return dp[house][color]

            min_cost = float('inf')
            for c in range(1, n + 1):
                if c != houses[house]:
                    min_cost = min(min_cost, dfs(house + 1, c, target - (c == houses[house - 1] if house > 0 else 0)) + cost[