from typing import List
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        m = len(evil)
        dp = [[[0]*2 for _ in range(m+1)] for _ in range(n+1)]
        dp[0][0][1] = 1
        last = {c: i for i, c in enumerate(evil)}
        max_last = max(last.values())
        for i in range(n):
            for j in range(m+1):
                for k in range(2):
                    for c in 'ab':
                        if k == 1 and c < s1[i]:
                            continue
                        if k == 1 and c > s2[i]:
                            break
                        ni, nj = i+1, j
                        if c == evil[j]:
                            nj += 1
                        if nj > m:
                            continue
                        if c == 'b':
                            continue
                        if nj == m and c > evil[nj-1]:
                            continue
                        if nj > max_last:
                            continue
                        dp[ni][nj][k or (c > s2[i])] += dp[i][j][k]
                        dp[ni][nj][k or (c > s2[i])] %= MOD
        return sum(dp[n][j][k] for j in range(m+1) for k in range(2)) % MOD