from typing import List
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0] * n
        dp[0] = 1
        ans = 0

        for i in range(1, n):
            dp[i] = dp[i - 1] | arr[i]
            ans += dp[i]

        return ans