from typing import List
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n
        dp[0] = arr[0]

        for i in range(1, n):
            dp[i] = max(dp[j] + arr[i] for j in range(i - k, i)) if k <= i else arr[i]

        return max(dp)