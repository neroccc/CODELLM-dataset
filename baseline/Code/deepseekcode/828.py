from typing import List
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = [-1] * 26
        preIndex = [-1] * 26
        res = 0
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(n):
            if index[ord(s[i]) - ord('A')] != -1:
                dp[i + 1] = dp[i] - dp[index[ord(s[i]) - ord('A')]] + i - index[ord(s[i]) - ord('A')] + 1
            else:
                dp[i + 1] = dp[i] + i - preIndex[ord(s[i]) - ord('A')] + 1
            res += dp[i + 1]
            preIndex[ord(s[i]) - ord('A')] = index[ord(s[i]) - ord('A')]
            index[ord(s[i]) - ord('A')] = i
        return res