from typing import List
class Solution:
    def minSubArrayLargestSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 1:
            return max(nums)

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            i = j = 0
            merged = []

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        sorted_nums = merge_sort(nums)
        ans = float('inf')

        for i in range(n - k + 1):
            ans = min(ans, sum(sorted_nums[i:i + k]))

        return ans