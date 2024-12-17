from typing import List
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos, neg = [0] * len(nums), [0] * len(nums)
        if nums[0] > 0:
            pos[0] = 1
        elif nums[0] < 0:
            neg[0] = 1
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos[i] = pos[i - 1] + 1
                neg[i] = neg[i - 1] + 1 if neg[i - 1] > 0 else 0
            elif nums[i] < 0:
                pos[i] = neg[i - 1] + 1 if neg[i - 1] > 0 else 0
                neg[i] = pos[i - 1] + 1
        return max(pos)