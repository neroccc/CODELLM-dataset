from typing import List
class Solution:
    def countArrangement(self, n: int) -> int:
        def dfs(i, used):
            if i == 1:
                return 1
            count = 0
            for j in range(1, n + 1):
                if (j % i == 0 or i % j == 0) and j not in used:
                    used.add(j)
                    count += dfs(i - 1, used)
                    used.remove(j)
            return count

        return dfs(n, set())