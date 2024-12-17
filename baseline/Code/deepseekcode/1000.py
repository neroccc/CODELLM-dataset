import heapq
from typing import List
class Solution:
    def minCost(self, stones: List[int], k: int) -> int:
        n = len(stones)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        min_heap = [(0, 0)]

        for i in range(1, n + 1):
            while min_heap[0][1] < i - k:
                heapq.heappop(min_heap)
            dp[i] = min_heap[0][0] + (prefix_sum[i] - prefix_sum[i - 1])
            heapq.heappush(min_heap, (dp[i], i))

        return dp[-1]