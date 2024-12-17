from typing import List
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        def get_sum(start, end):
            return prefix_sum[end + 1] - prefix_sum[start]

        left_sum = [0] * n
        right_sum = [0] * n
        left_max = 0
        right_max = 0
        for i in range(n):
            if i >= k:
                left_sum[i] = left_sum[i - 1] + get_sum(i - k, i)
            else:
                left_sum[i] = get_sum(0, i)
            if n - i - 1 >= k:
                right_sum[n - i - 1] = right_sum[n - i] + get_sum(n - i, n - i - k)
            else:
                right_sum[n - i - 1] = get_sum(n - i - k, n - 1)
            if i >= k:
                left_max = max(left_max, left_sum[i - k])
            if n - i - 1 >= k:
                right_max = max(right_max, right_sum[n - i - 1])

        ans = [0, 0, 0]
        max_sum = 0
        for i in range(k, n - 2 * k + 1):
            if left_sum[i - k] == left_max and right_sum[i + k] == right_max:
                cur_sum = left_sum[i - k] + get_sum(i, i + k - 1) + right_sum[i + k]
                if cur_sum