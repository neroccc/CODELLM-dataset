from typing import List
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0] * 3
        for num in nums:
            for i in range(3):
                dp[(i + num) % 3] = max(dp[(i + num) % 3], dp[i] + num)
        return dp[0]