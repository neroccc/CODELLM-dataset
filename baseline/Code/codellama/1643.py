from typing import List
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        m, n = destination
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        ans = ""
        for i in range(m, 0, -1):
            for j in range(n, 0, -1):
                if k <= dp[i][j]:
                    ans += "H" * j + "V" * i
                    return ans
                k -= dp[i][j]
                ans += "H" * j
        return ans
