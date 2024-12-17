from typing import List
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        ans = curr = sum(i * num for i, num in enumerate(nums))

        for i in range(1, n):
            curr += total - n * nums[n - i]
            ans = max(ans, curr)

        return ans