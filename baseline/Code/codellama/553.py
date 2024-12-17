from typing import List
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return str(nums[0]) + "/" + str(nums[1])
        ans = [0, 0]
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
            ans = [i, i]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                dp[i][j] = max(dp[i][j], dp[i + 1][j - 1])
                dp[i][j] = max(dp[i][j], dp[i][j - 1] / dp[i + 1][j])
                dp[i][j] = max(dp[i][j], dp[i + 1][j] / dp[i][j - 1])
                ans = [i, j]

        i, j = ans
        return str(dp[0][n - 1]) + ("/" if i else "") + "/".join(
            map(str, nums[i + 1 : j]))