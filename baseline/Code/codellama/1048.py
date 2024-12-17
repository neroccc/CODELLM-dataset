from typing import List
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = [1] * len(words)

        def isPredecessor(self, a, b):
            j = 0
            for i in range(len(a)):
                if a[i] != b[j]:
                    j += 1
                    if j == len(b):
                        return False
                if i == len(a) - 1:
                    return True
            return False
        for i in range(len(words)):
            for j in range(i):
                if len(words[i]) == len(words[j]) + 1 and isPredecessor(words[i], words[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
