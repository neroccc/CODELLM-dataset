from typing import List
class Solution:
    def countTeams(self, rating: List[int]) -> int:
        n = len(rating)
        dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if rating[i] < rating[j]:
                    dp[i][j][0] = 1
                elif rating[i] > rating[j]:
                    dp[i][j][1] = 1
                dp[i][j][2] = 1

        for k in range(2, n):
            for i in range(n - k):
                j = i + k
                for t in range(3):
                    for s in range(3):
                        if t != s:
                            dp[i][j][t] += dp[i][j - 1][s]

        return sum(dp[0][n - 1])