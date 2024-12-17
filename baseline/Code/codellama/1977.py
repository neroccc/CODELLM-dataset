from typing import List
class Solution:
    def getModifiedString(self, num: str) -> int:
        n = len(num)
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = 1
        for i in range(1, n):
            if num[i] != "0":
                dp[i][i] = dp[i - 1][i - 1]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if num[i] != "0":
                    dp[i][j] = (dp[i][j] + dp[i + 1][j]) % (10 ** 9 + 7)
        return dp[0][n - 1]