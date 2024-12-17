from typing import List
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        players = sorted(zip(scores, ages))
        dp = [0] * n
        for i in range(n):
            dp[i] = scores[i]

        for i in range(1, n):
            for j in range(i):
                if players[i][1] > players[j][1]:
                    dp[i] = max(dp[i], dp[j] + scores[i])

        return max(dp)