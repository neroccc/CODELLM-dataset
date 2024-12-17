from typing import List
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n, p = len(nums), [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            p[i] = p[i - 1] + nums[i - 1]
        dp, pos = [0] * (n + 1), [0] * (n + 1)
        for i in range(k, n + 1):
            if p[i] - p[i - k] > dp[i - 1]:
                dp[i] = p[i] - p[i - k]
                pos[i] = i - k
            else:
                dp[i] = dp[i - 1]
                pos[i] = pos[i - 1]
        ans, j = [0] * 3, n
        for idx in range(3):
            ans[2 - idx] = pos[j]
            j = pos[j] - k
        return ans