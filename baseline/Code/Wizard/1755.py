from typing import List
class Solution:
    def minAbsoluteSumDiff(self, nums: List[int], goal: int) -> int:
        nums.sort()
        n = len(nums)
        total = sum(nums)
        if total == goal:
            return 0
        elif total < goal:
            return goal - total
        elif total > goal:
            return total - goal

        if total % n == 0:
            return 0

        if total % n == 1:
            return min(abs(total - goal), abs(total - goal - 1))

        if total % n == 2:
            return min(abs(total - goal), abs(total - goal - 2))

        mid = total // n
        if n % 2 == 0:
            return min(abs(total - goal), abs(total - goal - 2 * mid))
        else:
            return min(abs(total - goal), abs(total - goal - 2 * mid), abs(total - goal - 2 * mid - 1))