from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target = total_sum // k
        used = [False] * len(nums)
        nums.sort(reverse=True)  # sort in descending order

        def backtrack(k: int, curr_sum: int, curr_num: int, used: List[bool]) -> bool:
            if k == 1:
                return True
            if curr_sum == target and curr_num > 0:
                return backtrack(k - 1, 0, 0, used)
            for i in range(len(nums)):
                if used[i] or curr_sum + nums[i] > target:
                    continue
                used[i] = True
                if backtrack(k, curr_sum + nums[i], curr_num + 1, used):
                    return True
                used[i] = False
            return False

        return backtrack(k, 0, 0, used)