from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i % 2][j] = dp[(i + 1) % 2][j] + 1
                elif nums[i] < nums[j]:
                    dp[i % 2][j] = max(dp[i % 2][j], dp[(i + 1) % 2][j] + 1)
                else:
                    dp[i % 2][j] = max(dp[i % 2][j], dp[(i + 1) % 2][j])
        return max(dp[0][i], dp[1][i])
