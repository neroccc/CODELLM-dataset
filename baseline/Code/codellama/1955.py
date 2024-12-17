from typing import List
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][nums[0]] = 1
        ans = 0

        for i in range(1, n):
            for j in range(3):
                if j == nums[i]:
                    dp[i][j] = dp[i - 1][j] + 1
                else:
                    dp[i][j] = dp[i - 1][j]

            ans += dp[i][nums[i]]

        return ans % (10 ** 9 + 7)
