from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        ans = 0

        for i in range(n):
            dp[i][i] = nums[i]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if nums[i] == nums[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = max(ans, diff + 1)

        return ans