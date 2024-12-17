from typing import List
class Solution:
    def countMaxOrSubstrings(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = 1
            for j in range(i):
                if arr[i] | arr[j] > arr[i]:
                    dp[i] += dp[j]

        return dp[-1]