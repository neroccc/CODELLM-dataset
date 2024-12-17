from typing import List
class Solution:
    def count_expressions(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[target]