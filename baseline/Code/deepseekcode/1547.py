from typing import List
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        dp = [[0]*len(cuts) for _ in range(len(cuts))]
        for l in range(2, len(cuts)):
            for i in range(len(cuts)-l):
                dp[i][i+l] = min(dp[i][k] + dp[k][i+l] for k in range(i+1, i+l)) + cuts[i+l] - cuts[i]
        return dp[0][-1]