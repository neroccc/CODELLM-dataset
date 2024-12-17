from typing import List
class Solution:
    def minJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        if n == 1:
            return 0

        dp = [0] * n
        for i in range(n):
            dp[i] = float('inf')
        dp[0] = 0
        dp[1] = 0 if obstacles[1] == 0 else float('inf')

        for i in range(2, n):
            if obstacles[i] == 0:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = float('inf')

        for i in range(2, n):
            for j in range(i):
                if obstacles[j] == 0 and obstacles[i] == 0:
                    dp[i] = min(dp[i], dp[j] + 1)

            for j in range(i + 1, n):
                if obstacles[j] == 0 and obstacles[i] == 0:
                    dp[j] = min(dp[j], dp[i] + 1)

        return dp[n - 1] if dp[n - 1] != float('inf') else -1