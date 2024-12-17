from typing import List
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'O' + dominoes + 'O'
        res = []
        i = 0
        for j in range(1, len(dominoes)):
            if dominoes[j] == '.':
                continue
            if i > 0:
                res.append(dominoes[i])
            diff = j - i - 1
            if dominoes[i] == dominoes[j]:
                res.append(dominoes[i] * diff)
            elif dominoes[i] == 'L' and dominoes[j] == 'R':
                res.append('.' * diff)
            else:
                middle = 'R' * (diff // 2) + '.' * (diff % 2) + 'L' * (diff // 2)
                res.append(middle)
            i = j
        return ''.join(res)