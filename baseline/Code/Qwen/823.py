from typing import List
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        dp = [1] * n
        index = {x: i for i, x in enumerate(arr)}

        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    k = arr[i] // arr[j]
                    if k in index:
                        dp[i] += dp[j] * dp[index[k]]

        return sum(dp) % (10 ** 9 + 7)