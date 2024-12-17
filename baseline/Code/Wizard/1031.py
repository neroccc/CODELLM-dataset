from typing import List
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        first_sum = [0] * n
        second_sum = [0] * n

        for i in range(1, n):
            first_sum[i] = first_sum[i - 1] + nums[i]
            second_sum[i] = second_sum[i - 1] + nums[i]

        max_sum = float('-inf')
        for i in range(n - firstLen):
            if i > 0:
                first_sum[i] = first_sum[i] - first_sum[i - 1]

        for i in range(firstLen, n - secondLen):
            if i > firstLen:
                first_sum[i] = first_sum[i] - first_sum[i - firstLen]

            max_sum = max(max_sum, first_sum[i] + second_sum[i + secondLen - 1])

        for i in range(n - secondLen - 1, -1, -1):
            if i + secondLen < n:
                second_sum[i] = second_sum[i + secondLen] - nums[i + secondLen]

        for i in range(n - firstLen - secondLen - 1, -1, -1):
            if i + firstLen < n:
                first_sum[i] = first_sum[i + firstLen] - nums[i + firstLen]

            max_sum = max(max_sum, first_sum[i] + second_sum[i + firstLen])

        return max_sum