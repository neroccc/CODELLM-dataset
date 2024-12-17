from typing import List
class Solution:
    def minOperations(self, arr1: List[int], arr2: List[int]) -> int:
        n1, n2 = len(arr1), len(arr2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(n1 + 1):
            dp[i][0] = i

        for j in range(n2 + 1):
            dp[0][j] = j

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if arr1[i - 1] == arr2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[n1][n2] if dp[n1][n2] < n1 else -1