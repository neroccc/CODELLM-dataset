from typing import List
class Solution:
    def waysToCutPizza(self, pizza: List[str], k: int) -> int:
        rows, cols = len(pizza), len(pizza[0])
        dp = [[0] * (k + 1) for _ in range(rows + 1)]
        dp[0][0] = 1
        for i in range(rows):
            for j in range(cols):
                if pizza[i][j] == 'A':
                    for cut in range(1, k + 1):
                        if i > 0:
                            dp[i][cut] += dp[i - 1][cut - 1]
                        if j > 0:
                            dp[i][cut] += dp[i][cut - 1]
        return dp[rows][k] % (10 ** 9 + 7)