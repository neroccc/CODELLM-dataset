from typing import List
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices) // 3
        slices.sort(reverse=True)
        return sum(slices[:n])