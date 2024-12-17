from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            if dp[i]:
                for j in range(i + 1, min(i + nums[i] + 1, n)):
                    dp[j] = True

        return dp[-1]