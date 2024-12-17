from typing import List
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        force = [0] * n
        ans = list(dominoes)

        for i in range(n):
            if ans[i] == 'L':
                force[i] = -1
            elif ans[i] == 'R':
                force[i] = 1

        right = 0
        for i in range(n - 1, -1, -1):
            if ans[i] == 'R':
                right = i
                break

        for i in range(n):
            if force[i] == 0:
                force[i] = right - i

        for i in range(n):
            if force[i] > 0:
                ans[i] = 'R'
            elif force[i] < 0:
                ans[i] = 'L'

        return "".join(ans)