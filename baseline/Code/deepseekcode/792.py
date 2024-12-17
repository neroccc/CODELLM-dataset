from typing import List
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos = {ch: [] for ch in set(s)}
        for i, ch in enumerate(s):
            pos[ch].append(i)

        res = len(words)
        for word in words:
            it = iter(pos[ch] for ch in word)
            try:
                idx = -1
                for arr in it:
                    idx = next(x for x in arr if x > idx)
            except StopIteration:
                res -= 1
        return res