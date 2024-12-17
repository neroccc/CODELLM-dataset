from typing import List
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1 + 1):
            dp[i][0] = i
        for j in range(n2 + 1):
            dp[0][j] = j

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

        i, j = n1, n2
        ans = ""
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                ans = str1[i - 1] + ans
                i -= 1
                j -= 1
            elif dp[i - 1][j] < dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        return str2[:j] + ans + str1[:i]