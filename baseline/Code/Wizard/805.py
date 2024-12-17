from typing import List
class Solution:
    def canBalance(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        nums.sort(reverse=True)
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return True
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

        return False