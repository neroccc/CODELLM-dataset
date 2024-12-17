from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        tails = [0] * n
        size = 0

        for num in nums:
            left, right = 0, size
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            tails[left] = num
            if left == size:
                size += 1

        return size