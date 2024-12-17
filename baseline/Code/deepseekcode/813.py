from typing import List
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        P = [0]
        for x in nums: P.append(P[-1] + x)
        dp = [P[-1]/len(nums) for _ in nums] + [0]
        for kk in range(k-1):
            dp = [max(dp[j] + (P[i]-P[j]) / (i-j) for i in range(j+1, len(nums)+1)) for j in range(len(nums))]
        return dp[0]