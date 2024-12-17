from typing import List
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        for i in range(len(nums)):
            dp[i] = {}
            for j in range(i):
                d = nums[i] - nums[j]
                if d in dp[j]:
                    dp[i][d] = dp[j][d] + 1
                else:
                    dp[i][d] = 2
        return max([max(dp[i].values()) for i in dp])