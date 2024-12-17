from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = [''] * (len(s) + 1)
        memo[-1] = [[]]

        for idx in range(len(s) - 1, -1, -1):
            paths = []
            for curr_idx in range(idx + 1, len(s) + 1):
                if s[idx:curr_idx] in wordDict:
                    for path in memo[curr_idx]:
                        paths.append((s[idx:curr_idx] + ' ' + path).strip())
            memo[idx] = paths

        return memo[0]