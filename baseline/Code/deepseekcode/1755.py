import bisect
from typing import List
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def get_sums(nums):
            n = len(nums)
            sums = {0}
            for num in nums:
                sums |= {x + num for x in sums}
            return sorted(list(sums))

        mid = len(nums) // 2
        left, right = get_sums(nums[:mid]), get_sums(nums[mid:])

        res = float('inf')
        for l in left:
            i = bisect.bisect_right(right, goal - l)
            if i < len(right):
                res = min(res, right[i] + l - goal)
            if i > 0:
                res = min(res, goal - right[i-1] - l)
            if res == 0:
                return 0
        return res