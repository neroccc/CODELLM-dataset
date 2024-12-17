from typing import List
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        def get_max_sum(first_len, second_len):
            max_sum = 0
            max_first_sum = 0
            for i in range(first_len + second_len - 1, n):
                if i >= firstLen:
                    max_first_sum = max(max_first_sum, prefix_sum[i - second_len + 1] - prefix_sum[i - second_len - firstLen])
                max_sum = max(max_sum, max_first_sum + prefix_sum[i + 1] - prefix_sum[i - second_len + 1])
            return max_sum

        return max(get_max_sum(firstLen, secondLen), get_max_sum(secondLen, firstLen))