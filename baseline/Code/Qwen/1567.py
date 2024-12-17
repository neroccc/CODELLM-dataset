from typing import List
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        pos = neg = 0
        ans = 0

        for num in nums:
            if num == 0:
                pos, neg = 0, 0
            elif num > 0:
                pos += 1
                neg = neg + 1 if neg else 0
            else:
                pos, neg = neg + 1 if neg else 0, pos + 1

            ans = max(ans, pos)

        return ans