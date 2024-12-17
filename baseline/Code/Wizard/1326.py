from typing import List
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = float('inf')

        for i in range(n + 1):
            left, right = max(0, i - ranges[i]), min(n, i + ranges[i])
            for j in range(left, right + 1):
                dp[j] = min(dp[j], dp[i - 1] + 1)

        for i in range(1, n + 1):
            if dp[i] == float('inf'):
                return -1

        return dp[n]