from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(s, start, path, res, wordDict):
            if start == len(s):
                res.append(" ".join(path))
                return
            for i in range(start, len(s)):
                if s[start:i + 1] in wordDict:
                    path.append(s[start:i + 1])
                    dfs(s, i + 1, path, res, wordDict)
                    path.pop()

        res = []
        dfs(s, 0, [], res, wordDict)
        return res