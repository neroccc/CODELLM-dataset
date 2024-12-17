from typing import List
class Solution:
    def minOperations(self, expression: str) -> int:
        n = len(expression)
        dp = [[float('inf')] * n for _ in range(n)]
        ans = 0

        for i in range(n):
            dp[i][i] = 0

        for i in range(n - 1):
            if expression[i] == expression[i + 1]:
                dp[i][i + 1] = 0
                ans = max(ans, dp[i][i + 1])

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if expression[i] == expression[j] and dp[i + 1