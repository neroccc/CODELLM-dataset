from typing import List
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[False] * n for _ in range(n)]
        next_greatest = [0] * n
        next_smallest = [0] * n
        max_val = float('-inf')
        min_val = float('inf')

        for i in range(n - 1, -1, -1):
            max_val = max(max_val, arr[i])
            dp[i][i] = True
            next_greatest[i] = i
            next_smallest[i] =