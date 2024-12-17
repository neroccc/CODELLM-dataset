from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[False] * n for _ in range(n)]
        dp[0][0] = True

        for i in range(1, n):
            for j in range(i):
                for k in range(j + 1, i + 1):
                    if stones[k] - stones[j] == k - j:
                        dp[i][k] = True

        return any(dp[-1])