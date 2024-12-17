from typing import List
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        dp = [[False] * n for _ in range(n)]
        ans = 0

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if tasks[i] <= sessionTime:
                dp[i][i + 1] = True
                ans += 1

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if tasks[i] + tasks[j] <= sessionTime and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans += 1

        return ans + (n > 1 and dp[0][n - 1])