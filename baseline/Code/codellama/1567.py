from typing import List
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        ans = 0

        for i in range(n):
            if nums[i] > 0:
                dp[i] = 1
                ans = max(ans, dp[i])
            elif nums[i] == 0:
                dp[i] = 0
            else:
                for j in range(i - 1, -1, -1):
                    if nums[j] > 0:
                        dp[i] = dp[j] + 1
                        break
                ans = max(ans, dp[i])

        return ans