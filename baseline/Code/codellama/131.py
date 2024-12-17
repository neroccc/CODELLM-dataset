from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = []

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True

        def dfs(s, path):
            if not s:
                ans.append(path)
                return

            for i in range(len(s)):
                if dp[0][i]:
                    dfs(s[i + 1 :], path + [s[0 : i + 1]])

        dfs(s, [])
        return ans