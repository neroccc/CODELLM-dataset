from typing import List
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger >= desiredTotal:
            return True
        if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
            return False

        dp = {}

        def canWin(nums, total):
            if total <= 0:
                return False
            key = tuple(nums)
            if key in dp:
                return dp[key]

            for i in range(len(nums)):
                if not canWin(nums[:i] + nums[i + 1 :], total - nums[i]):
                    dp[key] = True
                    return True

            dp[key] = False
            return False

        return canWin(list(range(1, maxChoosableInteger + 1)), desiredTotal)