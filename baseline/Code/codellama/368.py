from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = 1

        for diff in range(1, n):
            for i in range(n - diff):
                j = i + diff
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    dp[i][j] = max(dp[i][j], dp[i][i] + dp[j][j] + 1)
                    ans = [i, j] if dp[i][j] > dp[ans[0]][ans[1]] else ans

        i, j = ans
        return nums[i : j + 1]