from typing import List
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n, inf = len(jobDifficulty), float('inf')
        dp = [0] + [inf] * n
        if d > n:
            return -1
        for d in range(1, d + 1):
            stack = []
            for i in range(d - 1, n):
                dp[i + 1] = min(dp[j] + max(jobDifficulty[j:i + 1]) for j in range(i, -1, -1))
        return dp[-1]