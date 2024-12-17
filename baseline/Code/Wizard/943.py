from typing import List
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        def isSubstring(s1, s2):
            return s1 in s2

        def findLCS(s1, s2):
            m, n = len(s1), len(s2)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(m + 1):
                for j in range(n + 1):
                    if i == 0 or j == 0:
                        dp[i][j] = 0
                    elif s1[i - 1] == s2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = dp[i - 1][j]

            lcs = dp[-1][-1]
            return lcs

        def findMinLength(s1, s2):
            return len(s1) + len(s2) - 2 * findLCS(s1, s2)

        def findMinLengthString(s1, s2):
            lcs = findLCS(s1, s2)
            return s1[:lcs] + s2[lcs:]

        def findMinLengthStringHelper(words):
            n = len(words)
            if n == 1:
                return words[0]

            minLength = float('inf')
            minLengthString = ""
            for i in range(n):
                for j in range(n):
                    if i != j:
                        lcs = findMinLength(words[i], words[j])
                        minLengthString = min(minLengthString, findMinLengthString(words[i], words[j]), key=len)
                        minLength = min(minLength, lcs)

            return minLengthString

        words.sort(key=len, reverse=True)
        return findMinLengthStringHelper(words)