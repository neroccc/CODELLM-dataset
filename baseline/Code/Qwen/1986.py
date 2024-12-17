from typing import List
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        tasks.sort(reverse=True)
        dp = [[0] * (1 << n) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for mask in range(1 << n):
                dp[i][mask] = dp[i - 1][mask]
                for j in range(n):
                    if mask & (1 << j) == 0 and tasks[j] <= sessionTime:
                        dp[i][mask] = max(dp[i][mask], dp[i - 1][mask ^ (1 << j)] + tasks[j])

        for i in range(n + 1):
            if dp[i][(1 << n) - 1] >= sessionTime:
                return i

        return -1