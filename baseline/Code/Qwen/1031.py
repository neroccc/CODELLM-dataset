from typing import List
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def maxSum(firstLen, secondLen):
            max_sum = 0
            for i in range(firstLen + secondLen, n + 1):
                max_sum = max(max_sum, prefix[i] - prefix[i - secondLen] - prefix[firstLen] + prefix[firstLen - secondLen])
            return max_sum

        return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))