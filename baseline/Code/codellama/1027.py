from typing import List
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1] * n for _ in range(n)]
        ans = 1

        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[j] - nums[i] == 0:
                    dp[i][j] = dp[i][j - 1] + 1
                    ans = max(ans, dp[i][j])
                elif nums[j] - nums[i] == 1:
                    dp[i][j] = dp[i][j - 1] + 1
                    ans = max(ans, dp[i][j])
                elif nums[j] - nums[i] > 1:
                    dp[i][j] = 1

        return ans