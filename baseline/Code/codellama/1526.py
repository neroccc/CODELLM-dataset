from typing import List
class Solution:
    def minOperations(self, target: List[int]) -> int:
        n = len(target)
        dp = [[0] * n for _ in range(n)]
        ans = 0

        for i in range(n):
            dp[i][i] = 0

        for i in range(n - 1):
            if target[i] == target[i + 1]:
                dp[i][i + 1] = 0
                ans = max(ans, dp[i][i + 1])

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if target[i] == target[j] and dp[i + 1][j - 1]:
                    dp[i][j] = dp[i + 1][j - 1]
                    ans = max(ans, dp[i][j])

        return ans