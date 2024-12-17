from typing import List
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key = lambda x: len(x))
        ans = []
        for word in words:
            dp = [False] * (len(word) + 1)
            dp[0] = True
            for i in range(len(word)):
                if dp[i]:
                    for j in range(i + 1, len(word) + 1):
                        if j - i < len(word) and word[i:j] in words:
                            dp[j] = True
                            if j == len(word):
                                ans.append(word)
                                break
            if dp[-1]:
                ans.append(word)
        return ans