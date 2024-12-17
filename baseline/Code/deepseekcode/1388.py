from typing import List
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def solve(start, end):
            dp = [[0]*n for _ in range(m+1)]
            slices_ = [0] + slices[start:end]
            n = len(slices_)
            for i in range(2, n):
                for j in range(i-1, m, -1):
                    dp[j][i%2] = max(dp[j][(i-1)%2], dp[j-1][(i-1)%2] + slices_[i])
            return dp[m-1][(n-1)%2]

        n = len(slices)
        m = n // 3
        return max(solve(0, n-1), solve(1, n))