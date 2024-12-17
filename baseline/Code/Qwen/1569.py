from math import comb
from typing import List
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def dfs(nums):
            if len(nums) <= 2:
                return 1
            root = nums[0]
            left = [x for x in nums[1:] if x < root]
            right = [x for x in nums[1:] if x > root]
            return (
                dfs(left) * dfs(right) * comb(len(nums) - 1, len(left)) % MOD
            ) * 2 % MOD

        return (dfs(nums) - 1) % MOD