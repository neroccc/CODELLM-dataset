from typing import List
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        n = len(locations)
        dp = [[0] * n for _ in range(n)]
        dp[start][start] = 1

        for diff in range(1, fuel + 1):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        dp[i][j] = 1
                    elif diff >= abs(locations[i] - locations[j]):
                        dp[i][j] = (dp[i][j] + dp[i][j - 1]) % MOD

        ans = 0
        for i in range(n):
            if i != start:
                ans = (ans + dp[start][i]) % MOD

        return ans