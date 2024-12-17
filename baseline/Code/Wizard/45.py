from typing import List
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        if n == 2:
            return 1

        if nums[0] == n - 1:
            return 1

        if nums[0] == 0:
            return self.minJumps(nums[1:]) + 1

        if nums[-1] == 0:
            return self.minJumps(nums[:-1]) + 1

        max_reach = 0
        step = nums[0]
        for i in range(1, n):
            max_reach = max(max_reach, i + nums[i])
            if i == n - 1:
                break
            if max_reach >= n - 1:
                break

        if max_reach >= n - 1:
            return 1

        if max_reach < n - 1:
            return self.minJumps(nums[max_reach + 1:]) + 1

        if max_reach > n - 1:
            return self.minJumps(nums[1:]) + 1