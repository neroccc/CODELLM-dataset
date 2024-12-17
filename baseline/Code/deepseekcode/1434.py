from typing import List
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        mod = 10**9 + 7
        n, m = len(hats), 1<<len(hats)
        dp = [0]*m
        dp[0] = 1
        likes = [[] for _ in range(1,41)]
        for i in range(n):
            for hat in hats[i]:
                likes[hat].append(i)
        for hat in range(1,41):
            dp2 = dp[:]
            for people in range(m-1, -1, -1):
                for person in likes[hat]:
                    if (people & 1<<person) > 0:
                        dp2[people] = (dp2[people] + dp[people^1<<person]) % mod
            dp = dp2
        return dp[-1]