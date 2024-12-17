import collections
from typing import List

from deepseekcode.help.helphelp import isSubsequence


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_count = collections.Counter(words)
        ans = 0
        for word in word_count:
            if isSubsequence(word, s):
                ans += word_count[word]
        return ans

