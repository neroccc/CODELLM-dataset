from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            return s == s[::-1]

        def dfs(s, path):
            if not s:
                result.append(path)
                return
            for i in range(1, len(s) + 1):
                if isPalindrome(s[:i]):
                    dfs(s[i:], path + [s[:i]])

        result = []
        dfs(s, [])
        return result