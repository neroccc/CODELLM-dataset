from typing import List
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        force = [0] * n
        force[-1] = 0

        for i in range(n - 2, -1, -1):
            if dominoes[i] == 'R':
                force[i] = n
            elif dominoes[i] == 'L':
                force[i] = -n
            else:
                force[i] = max(force[i + 1], 0)

        for i in range(1, n):
            if dominoes[i] == '.' and force[i - 1] > 0:
                dominoes = dominoes[:i] + 'L' + dominoes[i:]
            elif dominoes[i] == '.' and force[i - 1] < 0:
                dominoes = dominoes[:i] + 'R' + dominoes[i:]

        return dominoes