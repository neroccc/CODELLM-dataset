from typing import List
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSubsequence(word: str) -> bool:
            t = 0
            for c in word:
                t = s.find(c, t) + 1
                if t == 0:
                    return False
            return True

        return sum(isSubsequence(word) for word in words)