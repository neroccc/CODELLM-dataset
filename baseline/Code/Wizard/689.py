from typing import List
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        for i in range(n - 1):
            dp[i][i + 1] = dp[i][i] + nums[i + 1]

        for diff in range(2, k + 1):
            for i in range(n - diff):
                j = i + diff
                dp[i][j] = float('-inf')
                for m in range(i, j):
                    dp[i][j] = max(dp[i][j], dp[i][m] + dp[m + 1][j])

        ans = [0] * 3
        for i in range(n - 2 * k):
            for j in range(i + k, n - k):
                for m in range(j + k, n):
                    if dp[i][j] + dp[j][m] > dp[ans[0]][ans[1]] + dp[ans[1] + 1][ans[2]]:
                        ans = [i, j, m]

        return ans