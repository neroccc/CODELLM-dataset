from typing import List
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        ans = 0

        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 1):
            for j in range(i + 1, n):
                if arr[j] - arr[i] in arr[i + 1 : j]:
                    dp[i][j] = dp[i + 1][j - 1] + 1
                    ans = max(ans, dp[i][j])

        return ans + 1 if ans else 0