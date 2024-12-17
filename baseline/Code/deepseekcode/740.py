from typing import List
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = [0] * (max(nums) + 1)
        for num in nums:
            freq[num] += num
        dp = [0, 0]
        for i in range(2, len(freq)):
            dp.append(max(dp[-1], dp[-2] + freq[i]))
        return dp[-1]