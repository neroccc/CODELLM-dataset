from typing import List
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        if total_sum % 3 == 0:
            return total_sum

        nums.sort(reverse=True)
        a, b, c = 0, 0, 0
        for num in nums:
            if num % 3 == 1:
                a += num
            elif num % 3 == 2:
                b += num
            else:
                c += num

        if total_sum - a - b - c < 0:
            return total_sum - a - b - c
        elif (total_sum - a - b - c) % 3 == 0:
            return total_sum - a - b - c
        else:
            return total_sum - max(a, b, c)