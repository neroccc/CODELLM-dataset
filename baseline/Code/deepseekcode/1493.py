from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        zero_count = 0
        ans = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            ans = max(ans, right - left)
            right += 1

        return ans if ans == len(nums) else ans + 1