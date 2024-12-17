from typing import List
class Solution:
    def maxHeight(self, rods: List[int]) -> int:
        rods.sort()
        left, right = 0, len(rods) - 1
        total = sum(rods)
        while left < right:
            if rods[left] + rods[right] > total // 2:
                return total // 2 - rods[left]
            else:
                left += 1
                right -= 1
        return total // 2