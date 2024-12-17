from typing import List
class Solution:
    def longestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        dp = [1] * n
        for i in range(n):
            for j in range(i + 1, n):
                if pairs[j][0] > pairs[i][1]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)