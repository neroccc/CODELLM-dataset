from typing import List
class Solution:
    def countArrangement(self, n: int) -> int:
        def dfs(i):
            if i == n + 1:
                self.ans += 1
                return
            for j in range(1, n + 1):
                if not used[j] and (i % j == 0 or j % i == 0):
                    used[j] = True
                    dfs(i + 1)
                    used[j] = False

        self.ans = 0
        used = [False] * (n + 1)
        dfs(1)
        return self.ans