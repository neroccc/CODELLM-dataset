from typing import List
class Solution:
    def maxSumDivByThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]
        for num in nums:
            dp = [max(dp[i], num + dp[(i-num)%3]) for i in range(3)]
        return dp[0]