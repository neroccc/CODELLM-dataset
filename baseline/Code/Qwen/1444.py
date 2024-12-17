from typing import List
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1] - dp[i + 1][j + 1] + (pizza[i][j] == 'A')
        ans = 0
        for i in range(m):
            for j in range(n):
                if pizza[i][j] == 'A':
                    for ni in range(i + 1, m):
                        if dp[i][j] - dp[ni][j] > 0:
                            ans = (ans + self.dfs(dp, ni, j, m, n, k - 1)) % MOD
                    for nj in range(j + 1, n):
                        if dp[i][j] - dp[i][nj] > 0:
                            ans = (ans + self.dfs(dp, i, nj, m, n, k - 1)) % MOD
        return ans

    def dfs(self, dp, i, j, m, n, k):
        if k == 0:
            return 1
        ans = 0
        for ni in range(i + 1, m):
            if dp[i][j] - dp[ni][j] > 0:
                ans = (ans + self.dfs(dp, ni, j, m, n, k - 1)) % 10**9 + 7
        for nj in range(j + 1, n):
            if dp[i][j] - dp[i][nj]