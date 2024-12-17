from typing import List

from deepseekcode.help.helphelp import check_subset_sum


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        nums.sort()

        for i in range(1, n // 2 + 1):
            if total_sum * i % n == 0:
                target = total_sum * i // n
                if check_subset_sum(nums, target, i):
                    return True

        return False
