from typing import List
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            next_multiple_of_2 = ugly[i2] * 2
            next_multiple_of_3 = ugly[i3] * 3
            next_multiple_of_5 = ugly[i5] * 5
            next_ugly_number = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
            ugly.append(next_ugly_number)

            if next_multiple_of_2 == next_ugly_number:
                i2 += 1
            if next_multiple_of_3 == next_ugly_number:
                i3 += 1
            if next_multiple_of_5 == next_ugly_number:
                i5 += 1

        return ugly[-1]