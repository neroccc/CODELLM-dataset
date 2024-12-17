from typing import List
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        dp = [[False] * (sessionTime + 1) for _ in range(n)]
        dp[0][tasks[0]] = True

        for i in range(1, n):
            for j in range(1, sessionTime + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= tasks[i]:
                    dp[i][j] |= dp[i - 1][j - tasks[i]]

        for j in range(sessionTime, 0, -1):
            if dp[n - 1][j]:
                return j

        return 1