from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        dp[0] = [[]]

        for i in range(n):
            for j in range(i + 1, n + 1):
                if s[i:j] in wordDict:
                    for prefix in dp[i]:
                        dp[j].append(prefix + [s[i:j]])

        return [" ".join(sentence) for sentence in dp[n]]