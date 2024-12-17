from typing import List
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = arr[0]
        dp[0][1] = arr[0]
        ans = arr[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i])
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i])
            ans = max(ans, dp[i][0], dp[i][1])

        return ans