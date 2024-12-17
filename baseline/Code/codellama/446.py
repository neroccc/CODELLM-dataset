from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        ans = 0

        for i in range(n):
            dp[i][i] = 1

        for diff in range(1, n):
            for i in range(n - diff):
                j = i + diff
                if nums[j] - nums[i] == nums[i + 1] - nums[j - 1]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    ans += dp[i][j]

        return ans
