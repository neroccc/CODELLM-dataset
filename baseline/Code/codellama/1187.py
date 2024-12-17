from typing import List
class Solution:
    def findMinMoves(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        if n != len(arr2):
            return -1
        total = sum(arr1) - sum(arr2)
        if total % n != 0:
            return -1
        avg = total // n
        ans = 0
        for i in range(n):
            ans += abs(arr1[i] - avg)
        return ans