from typing import List
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
            return False
        self.memo = {}
        return self.helper(range(1, maxChoosableInteger + 1), desiredTotal)

    def helper(self, nums, desiredTotal):
        hash = str(nums)
        if hash in self.memo:
            return self.memo[hash]

        if nums and nums[-1] >= desiredTotal:
            return True

        for i in range(len(nums) - 1, -1, -1):
            if not self.helper(nums[:i] + nums[i + 1:], desiredTotal - nums[i]):
                self.memo[hash] = True
                return True

        self.memo[hash] = False
        return False