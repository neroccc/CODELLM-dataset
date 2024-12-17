from functools import cache
from typing import List
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        @cache
        def dp(i, k):
            if k == 1:
                return (prefix_sum[n] - prefix_sum[i]) / (n - i)
            res = 0
            for j in range(i + 1, n):
                res = max(res, (prefix_sum[j] - prefix_sum[i]) / (j - i) + dp(j, k - 1))
            return res

        return dp(0, k)