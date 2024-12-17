from typing import List
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        people = [set() for _ in range(40)]
        for i, hat_list in enumerate(hats):
            for hat in hat_list:
                people[hat - 1].add(i)

        dp = [[0] * (1 << n) for _ in range(41)]
        dp[0][0] = 1

        for hat in range(1, 41):
            for mask in range(1 << n):
                for person in people[hat - 1]:
                    if mask & (1 << person) == 0:
                        dp[hat][mask | (1 << person)] += dp[hat - 1][mask]
                        dp[hat][mask | (1 << person)] %= (10 ** 9 + 7)

        return dp[40][(1 << n) - 1]