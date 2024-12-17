from typing import List
class Solution:
    def closestToTarget(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[float('inf')] * n for _ in range(n)]
        dp[0][0] = abs(nums[0] - target)
        ans = float('inf')

        for i in range(n):
            for j in range(i + 1):
                if i == j:
                    dp[i][j] = abs(nums[i] - target)
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + abs(nums[i] - nums[j])
                ans = min(ans, dp[i][j])

        return ans