from typing import List
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0] + [-1] * target
        for i in range(1, target + 1):
            for num, c in enumerate(cost):
                if i >= c and dp[i - c] != -1:
                    dp[i] = max(dp[i], dp[i - c] * 10 + num + 1)
        return str(dp[-1]) if dp[-1] != -1 else '0'