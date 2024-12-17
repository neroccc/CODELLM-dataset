from typing import List
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n, s = len(nums), sum(nums)
        dp = [set() for _ in range(n + 1)]
        dp[0].add(0)
        for num in nums:
            for i in range(n, 0, -1):
                for prev in dp[i - 1]:
                    dp[i].add(prev + num)
        for i in range(1, n + 1):
            if s * i % n == 0 and s * i / n in dp[i]:
                return True
        return False