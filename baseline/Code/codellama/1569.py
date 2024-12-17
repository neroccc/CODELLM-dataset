from typing import List
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = 1
        for i in range(1, n):
            dp[i][i] = 1
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                dp[i][j] = dp[i + 1][j - 1]
        return sum(dp[0]) % (10 ** 9 + 7)
