from typing import List
class Solution:
    def minSubArrayLen(self, arr: List[int], target: int) -> int:
        n = len(arr)
        left, right = 0, 0
        curr_sum = 0
        min_len = float('inf')
        ans = -1

        while right < n:
            curr_sum += arr[right]

            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= arr[left]
                left += 1

            right += 1

        return min_len if min_len != float('inf') else -1