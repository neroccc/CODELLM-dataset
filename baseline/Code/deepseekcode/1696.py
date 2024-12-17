from collections import deque
from typing import List
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        q = deque([0])

        for i in range(1, n):
            while q and q[0] < i - k:
                q.popleft()
            dp[i] = nums[i] + dp[q[0]]
            while q and dp[q[-1]] < dp[i]:
                q.pop()
            q.append(i)

        return dp[-1]