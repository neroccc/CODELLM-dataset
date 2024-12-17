from typing import List
class Solution:
    def maxAverageOfSubarrays(self, nums: List[int], k: int) -> float:
        n = len(nums)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]

        def get_average(l: int, r: int) -> float:
            return (presum[r] - presum[l]) / (r - l)

        def get_max_average(i: int, j: int) -> float:
            return max(get_average(i, mid) for mid in range(i, j + 1))

        ans = 0.0
        for i in range(k, n + 1):
            ans = max(ans, get_max_average(i - k, i))

        return ans