from typing import List
class Solution:
    def paint(self, cost, target):
        n = len(cost)
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= cost[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - cost[i - 1]] + cost[i - 1])

        i, j = n, target
        ans = ""
        while i > 0 and j > 0:
            if dp[i][j] == dp[i - 1][j]:
                i -= 1
            else:
                ans += str(i)
                j -= cost[i - 1]
                i -= 1

        return ans[::-1] if ans else "0"