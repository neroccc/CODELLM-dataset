from typing import List
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n = len(s)
        dp = [0] * len(words)
        for i in range(n):
            for j in range(len(words)):
                if dp[j] == 0 and s[i] == words[j][dp[j]]:
                    dp[j] += 1
        return sum(dp)