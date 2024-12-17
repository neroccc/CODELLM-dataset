from typing import List
class Solution:
    def findIntegers(self, n: int) -> int:
        binary = bin(n)[2:]
        length = len(binary)
        dp = [[0, 0] for _ in range(length+1)]
        dp[0][0] = dp[0][1] = 1
        for i in range(1, length+1):
            if binary[i-1] == '0':
                dp[i][0] = dp[i-1][0] + dp[i-1][1]
                dp[i][1] = dp[i-1][1]
            else:
                dp[i][0] = dp[i-1][0] + dp[i-1][1]
                dp[i][1] = dp[i-1][0]
        return max(dp[-1])