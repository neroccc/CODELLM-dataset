from typing import List
class Solution:
    def max_value(self, nums: List[int]) -> str:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = str(nums[i])

        for diff in range(1, n):
            for i in range(n - diff):
                j = i + diff
                for k in range(i, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + "/" + dp[k + 1][j], key=lambda x: eval(x))

        return dp[0][-1]