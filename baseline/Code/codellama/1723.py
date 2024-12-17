from typing import List
class Solution:
    def maxJob(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        jobs.sort(reverse=True)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = jobs[i]

        for diff in range(2, n + 1):
            for i in range(n - diff + 1):
                j = i + diff - 1
                dp[i][j] = max(jobs[i : j + 1])

        return sum(dp[i][i + k - 1] for i in range(n - k + 1))