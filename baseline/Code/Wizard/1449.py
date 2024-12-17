from typing import List
class Solution:
    def maxNumber(self, cost: List[int], target: int) -> str:
        dp = [[0] * (target + 1) for _ in range(9)]
        for i in range(9):
            dp[i][0] = 1

        for i in range(1, 9):
            for j in range(1, target + 1):
                if j >= cost[i]:
                    dp[i][j] = dp[i - 1][j]
                    if dp[i - 1][j - cost[i]] + 1 > dp[i][j]:
                        dp[i][j] = dp[i - 1][j - cost[i]] + 1

        for i in range(9, 0, -1):
            if dp[i][target]:
                ans = str(i) * dp[i][target]
                return ans

        return "0 "