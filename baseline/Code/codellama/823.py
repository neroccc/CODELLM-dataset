from typing import List
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0] * n
        arr.sort()

        for i in range(n):
            dp[i] = 1
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    dp[i] += dp[j] * dp[arr.index(arr[i] // arr[j])]
            dp[i] %= (10 ** 9 + 7)

        return sum(dp) % (10 ** 9 + 7)
