from typing import List
class Solution:
    def longestWordChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = [1] * len(words)
        max_len = 1

        for i in range(len(words)):
            for j in range(i):
                if len(words[i]) == len(words[j]) + 1:
                    for k in range(len(words[j])):
                        if words[i][:k] + words[i][k + 1:] == words[j]:
                            dp[i] = max(dp[i], dp[j] + 1)
                            max_len = max(max_len, dp[i])

        return max_len