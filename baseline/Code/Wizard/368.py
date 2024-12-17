from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort(reverse=True)
        dp = [1] * n
        parent = [-1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        parent[i] = j

        max_len = max(dp)
        max_idx = dp.index(max_len)
        answer = []
        while max_idx != -1:
            answer.append(nums[max_idx])
            max_idx = parent[max_idx]

        return answer[::-1]