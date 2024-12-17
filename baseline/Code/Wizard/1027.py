from typing import List
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1] * n for _ in range(n)]
        max_len = 1

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                for k in range(j):
                    if nums[i] - nums[k] == diff:
                        dp[i][j] = dp[k][j] + 1
                        max_len = max(max_len, dp[i][j])

        for i in range(n):
            for j in range(i + 1, n):
                diff = nums[j] - nums[i]
                for k in range(i):
                    if nums[j] - nums[k] == diff:
                        dp[j][i] = dp[k][i] + 1
                        max_len = max(max_len, dp[j][i])

        return max_len + 1