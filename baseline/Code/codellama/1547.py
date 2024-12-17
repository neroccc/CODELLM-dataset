import math
from typing import List
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.insert(0, 0)
        cuts.append(n)
        n += 1
        dp = [0] * n
        for i in range(2, n):
            dp[i] = math.inf
            for j in range(i):
                dp[i] = min(dp[i], dp[j] + abs(cuts[j] - cuts[i]))
        return dp[-1]