from typing import List
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = [1]
        i2, i3, i5 = 0, 0, 0
        next_2 = 2
        next_3 = 3
        next_5 = 5

        for _ in range(1, n):
            min_val = min(next_2, next_3, next_5)
            ugly_nums.append(min_val)

            if min_val == next_2:
                i2 += 1
                next_2 = ugly_nums[i2] * 2
            if min_val == next_3:
                i3 += 1
                next_3 = ugly_nums[i3] * 3
            if min_val == next_5:
                i5 += 1
                next_5 = ugly_nums[i5] * 5

        return ugly_nums[-1]