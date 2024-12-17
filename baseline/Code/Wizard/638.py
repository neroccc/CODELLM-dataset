from typing import List
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        m = len(special)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[0][i] = 0

        for i in range(n):
            dp[i][0] = 0

        for i in range(1, n + 1):
            dp[i][1] = price[i - 1] * needs[i - 1]

        for i in range(2, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= i:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - i] + i * price[i - 1])

        for offer in special:
            for j in range(n, 0, -1):
                for k in range(j, 0, -1):
                    if k >= offer[-2]:
                        dp[j] = [min(dp[j], dp[k] + offer[-1])]

        return min(dp[n])