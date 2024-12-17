from typing import List
class Solution:
    def maxSubarraySumWithOneDeletion(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

        ans = dp[n - 1]
        for i in range(n - 3, -1, -1):
            dp[i] = max(dp[i + 1], dp[i + 2] + arr[i])
            ans = max(ans, dp[i])

        return ans