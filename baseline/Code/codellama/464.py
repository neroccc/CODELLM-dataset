from typing import List
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True
        memo = {}
        return self.helper(maxChoosableInteger, desiredTotal, 0, memo)

    def helper(self, maxChoosableInteger, desiredTotal, currentSum, memo):
        if currentSum in memo:
            return memo[currentSum]
        if currentSum >= desiredTotal:
            return False
        for i in range(1, maxChoosableInteger + 1):
            if i not in memo:
                if not self.helper(maxChoosableInteger, desiredTotal, currentSum + i, memo):
                    memo[currentSum] = True
                    return True
        memo[currentSum] = False
        return False