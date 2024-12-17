from typing import List
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        deque = deque([0])

        for i in range(1, n):
            while deque and deque[0] < i - k:
                deque.popleft()
            dp[i] = dp[deque[0]] + nums[i]
            while deque and dp[deque[-1]] <= dp[i]:
                deque.pop()
            deque.append(i)

        return dp[-1]