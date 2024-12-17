from typing import List
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    for overlap_len in range(1, min(len(words[i]), len(words[j]))):
                        if words[i].endswith(words[j][:overlap_len]):
                            overlap[i][j] = overlap_len

        dp = [[0] * n for _ in range(n)]
        parent = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][(1 << i) % n] = len(words[i])
        for code in range(1, 1 << n):
            if bin(code).count('1') == 1:
                for i in range(n):
                    if (1 << i) & code:
                        dp[i][code] = len(words[i])
            else:
                for i in range(n):
                    if (1 << i) & code:
                        prev_code = code ^ (1 << i)
                        min_len = min((dp[j][prev_code] + len(words[j]) - overlap[j][i] for j in range(n) if (1 << j) & code), default=0)
                        dp[i][code] = min_len + len(words[i])
        min_len = min(dp[i][(1 << n) - 1] for i in range(n))
        code = (1 << n) - 1
        i = dp.index(min_len, 0, n)
        ans = words[i]
        while code != (1 << i):
            j = dp[i][code] - len(words[i]) + overlap[i][parent[i][code]]
            ans += words[i][j:]
            code = parent[i][code]
            i = parent[i