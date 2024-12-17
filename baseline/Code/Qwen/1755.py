from typing import List
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        left_sums = []
        right_sums = []

        def generate_sums(arr, sums):
            for i in range(1 << n):
                total = 0
                for j in range(n):
                    if i & (1 << j):
                        total += arr[j]
                sums.append(total)

        generate_sums(nums[: n // 2], left_sums)
        generate_sums(nums[n // 2 :], right_sums)

        left_sums.sort()
        right_sums.sort()

        result = abs(goal)
        left_index = 0
        right_index = len(right_sums) - 1

        while left_index < len(left_sums) and right_index >= 0:
            total = left_sums[left_index] + right_sums[right_index]
            result = min(result, abs(goal - total))

            if total < goal:
                left_index += 1
            else:
                right_index -= 1

        return result