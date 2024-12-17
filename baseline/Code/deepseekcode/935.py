from typing import List
class Solution:
    def knightDialer(self, n: int) -> int:
        phone = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]
        dp = [1] * 10
        for i in range(n - 1):
            dp2 = [0] * 10
            for j in range(10):
                for k in phone[j]:
                    dp2[k] += dp[j]
                    dp2[k] %= (10**9 + 7)
            dp = dp2
        return sum(dp) % (10**9 + 7)