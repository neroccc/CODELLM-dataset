from typing import List
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + houses[i]
        cost = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                mid = (i+j) // 2
                cost[i][j] = houses[mid]*(mid-i+1)-(prefix[mid+1]-prefix[i])
                cost[i][j] += (prefix[j+1]-prefix[mid+1])-houses[mid]*(j-mid)
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for j in range(1, n+1):
            for i in range(j):
                if dp[i] != float('inf'):
                    dp[j] = min(dp[j], dp[i]+cost[i][j-1]+(k>1))
        return dp[-1]-1 if n>k else 0