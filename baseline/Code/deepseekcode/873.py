from typing import List
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}
        dp = [[2] * len(arr) for _ in arr]
        for j, x in enumerate(arr):
            for i in range(j):
                if x - arr[i] < arr[i] and x - arr[i] in index:
                    dp[i][j] = dp[index[x - arr[i]]][i] + 1
        return max(x for row in dp for x in row) if max(x for row in dp for x in row) > 2 else 0