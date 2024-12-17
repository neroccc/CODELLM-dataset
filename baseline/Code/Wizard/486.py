from typing import List
class Solution:
    def canIWin(self, nums: List[int], target: int) -> bool:
        def helper(nums, target, memo):
            if sum(nums) < target:
                return False
            if target <= 0:
                return True
            if tuple(nums) in memo:
                return memo[tuple(nums)]
            for i in range(len(nums)):
                if not helper(nums[:i] + nums[i+1:], target - nums[i], memo):
                    memo[tuple(nums)] = True
                    return True
            memo[tuple(nums)] = False
            return False

        return helper(nums, target, {})