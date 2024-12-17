from typing import List
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        dp = [1] * n
        for i in range(1, n):
            dp[i] = (dp[i - 1] * (n - i)) / i
        return dp[-1]