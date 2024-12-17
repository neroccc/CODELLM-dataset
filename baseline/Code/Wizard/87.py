from typing import List
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        n = len(s1)
        if sorted(s1) != sorted(s2):
            return False

        def scramble(s1, s2):
            if len(s1) == 1:
                return s1 == s2

            for i in range(1, n):
                if (scramble(s1[:i], s2[:i]) and scramble(s1[i:], s2[i:])) or (scramble(s1[:i], s2[-i:]) and scramble(s1[i:], s2[:-i])):
                    return True

            return False

        return scramble(s1, s2)