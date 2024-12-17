from typing import List
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        first = [0] * n
        second = [0] * n
        first[0] = nums[0]
        second[0] = nums[0]
        for i in range(1, n):
            first[i] = max(first[i - 1] + nums[i], nums[i])
            second[i] = max(second[i - 1] + nums[i], nums[i])

        maxSum = first[firstLen - 1] + second[secondLen - 1]
        for i in range(firstLen + secondLen, n):
            maxSum = max(maxSum, first[i - firstLen] + second[i - secondLen])

        return maxSum