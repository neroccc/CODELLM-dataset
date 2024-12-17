from typing import List
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        dp = [False] * (total // 2 + 1)
        dp[0] = True
        for stone in stones:
            for i in range(total // 2, stone - 1, -1):
                dp[i] = dp[i] or dp[i - stone]
        for i in range(total // 2, -1, -1):
            if dp[i]:
                return total - 2 * i
        return total