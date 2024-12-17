from typing import List
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[2] * n for _ in range(n)]
        index = {x: i for i, x in enumerate(arr)}
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                k = index.get(arr[j] - arr[i], -1)
                if k >= 0 and k < i:
                    dp[i][j] = dp[k][i] + 1
                    ans = max(ans, dp[i][j])

        return ans if ans > 2 else 0