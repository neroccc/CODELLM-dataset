from typing import List
class Solution:
    def cutPizza(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        rows, cols = len(pizza), len(pizza[0])
        dp = [[0] * (k + 1) for _ in range(rows + 1)]

        for i in range(rows):
            for j in range(cols):
                if pizza[i][j] == 'A':
                    dp[i + 1][1] += 1

        for i in range(1, rows + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j]

        for j in range(1, cols + 1):
            for i in range(1, rows + 1):
                if pizza[i - 1][j - 1] == 'A':
                    dp[i][1] += dp[i - 1][j - 1]
                dp[i][j] = dp[i][j - 1]

        for i in range(1, rows + 1):
            for j in range(2, k + 1):
                for l in range(1, i + 1):
                    dp[i][j] += dp[l][j - 1]

        return dp[rows][k] % MOD