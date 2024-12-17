from typing import List
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0] * n
        dp[0] = arr[0]
        ans = arr[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1] + arr[i], arr[i])
            ans = max(ans, dp[i])

        return ans