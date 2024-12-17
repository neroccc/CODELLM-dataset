from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        stack = []
        res = 0

        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                j = stack.pop()
                for k in range(i - 1, j - 1, -1):
                    dp[k][i] += dp[k][j]
            stack.append(i)

            for j in stack:
                dp[i][j] = (dp[i][j - 1] + arr[i]) % (10 ** 9 + 7)

        for i in range(n):
            res = (res + dp[i][i]) % (10 ** 9 + 7)

        return res