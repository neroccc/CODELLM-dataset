from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False

        target = total_sum // k
        nums.sort(reverse=True)
        dp = [[False] * (target + 1) for _ in range(k)]

        for i in range(k):
            dp[i][0] = True

        for num in nums:
            for j in range(k):
                for i in range(target, -1, -1):
                    if i >= num:
                        dp[j][i] |= dp[j][i - num]
                    if dp[j][i]:
                        break

        return dp[-1][-1]