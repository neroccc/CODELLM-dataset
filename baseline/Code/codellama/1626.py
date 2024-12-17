from typing import List
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = (scores[0], ages[0])
        ans = 0

        for i in range(1, n):
            dp[i][i] = (scores[i], ages[i])
            if scores[i] > ans:
                ans = scores[i]

        for diff in range(2, n + 1):
            for i in range(n - diff + 1):
                j = i + diff - 1
                if scores[i] + scores[j] > ans:
                    ans = scores[i] + scores[j]
                    dp[i][j] = (scores[i], ages[i])

        i, j = 0, n - 1
        while i < j:
            if dp[i][j][1] < dp[i + 1][j][1]:
                i += 1
            else:
                j -= 1

        return ans