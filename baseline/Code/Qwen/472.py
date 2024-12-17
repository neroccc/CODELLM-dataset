from typing import List
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        def dfs(word):
            if word in words:
                return True
            for i in range(1, len(word)):
                if word[:i] in words and dfs(word[i:]):
                    return True
            return False
        return [word for word in words if dfs(word)]