from typing import List
class Solution:
    def maxScoreIndices(self, nums: List[int], multipliers: List[int]) -> List[int]:
        n = len(nums)
        m = len(multipliers)
        dp = [[0] * n for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 0
        for i in range(1, m + 1):
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + multipliers[i - 1] * nums[j - 1])
        i = m
        j = n - 1
        ans = [0, 0]
        while i > 0 and j > 0:
            if dp[i][j] == dp[i][j - 1]:
                j -= 1
            else:
                i -= 1
                j -= 1
                ans = [j + 1, i]
        return ans