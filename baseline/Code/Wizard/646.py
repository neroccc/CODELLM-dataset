from typing import List
class Solution:
    def longestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        n = len(pairs)
        dp = [1] * n
        ans = 1

        for i in range(1, n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])

        return ans