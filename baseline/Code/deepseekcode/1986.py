from typing import List
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        tasks.sort()
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            total = 0
            for i in range(n):
                if ((mask >> i) & 1) == 1:
                    total += tasks[i]
            if total <= sessionTime:
                dp[mask] = 1
        for mask in range(1, 1 << n):
            sub = mask
            while sub:
                if dp[sub] + dp[mask ^ sub] < dp[mask]:
                    dp[mask] = dp[sub] + dp[mask ^ sub]
                sub = (sub - 1) & mask
        return dp[-1]