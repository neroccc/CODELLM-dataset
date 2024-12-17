from typing import List
class Solution:
    def numberOfWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        mod = 10**9 + 7
        dp = [[0] * 41 for _ in range(1 << n)]
        dp[1 << 0][0] = 1

        for i in range(1, n + 1):
            for state in range(1, 1 << n):
                for hat in hats[i - 1]:
                    for prev_state in range(state):
                        if not (state & (1 << (i - 1)):
                            continue
                        dp[state][hat] += dp[prev_state]
                        dp[state][hat] %= mod

        ans = 0
        for state in range(1, 1 << n):
            count = 0
            for hat in range(41):
                if dp[state][hat]:
                    count += 1
            if count == n:
                ans += dp[state][0]
                ans %= mod

        return ans