from typing import List
class Solution:
    def minDays(self, n: int) -> int:
        if n == 1:
            return 1
        if n % 2 == 0 or n % 3 == 0:
            return 1
        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            if mid >= n:
                high = mid
            else:
                low = mid + 1
        return low