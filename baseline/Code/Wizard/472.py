from typing import List
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def isConcatenated(word, memo):
            if word in memo:
                return memo[word]
            if not word:
                return False
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in memo and memo[prefix] or suffix in memo and isConcatenated(suffix, memo):
                    memo[word] = True
                    return True
            memo[word] = False
            return False

        memo = {}
        for word in words:
            memo[word] = True

        result = []
        for word in words:
            if isConcatenated(word, memo):
                result.append(word)

        return result