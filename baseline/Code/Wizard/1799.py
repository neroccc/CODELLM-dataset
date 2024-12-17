import math
from typing import List
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums) // 2
        nums.sort(reverse=True)
        ans = 0

        for i in range(n):
            ans += (i + 1) * math.gcd(nums[i], nums[n + i])

        return ans