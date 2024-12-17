from typing import List
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        f = sum(i * num for i, num in enumerate(nums))
        ans = f
        s = sum(nums)
        for i in range(n - 1, 0, -1):
            f += s - n * nums[i]
            ans = max(ans, f)
        return ans