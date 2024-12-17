from typing import List
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        dp = [0] * n
        dp[0] = target[0]

        for i in range(1, n):
            if target[i] > target[i - 1]:
                dp[i] = dp[i - 1] + target[i] - target[i - 1]
            else:
                dp[i] = dp[i - 1]

        return dp[-1]