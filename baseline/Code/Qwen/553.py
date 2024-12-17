from typing import List
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return str(nums[0]) + "/" + str(nums[1])
        ans = str(nums[0]) + "/(" + str(nums[1])
        for i in range(2, n):
            ans += "/" + str(nums[i])
        ans += ")"
        return ans