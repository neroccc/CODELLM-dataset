from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s: str) -> bool:
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(s: str, start: int, path: List[str], res: List[List[str]]):
            if start == len(s):
                res.append(path[:])
                return

            for i in range(start, len(s)):
                if is_palindrome(s[start:i + 1]):
                    path.append(s[start:i + 1])
                    dfs(s, i + 1, path, res)
                    path.pop()

        res = []
        dfs(s, 0, [], res)
        return res