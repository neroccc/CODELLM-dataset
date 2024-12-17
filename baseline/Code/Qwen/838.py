from typing import List
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        left = [-1] * n
        right = [n] * n
        for i in range(n):
            if dominoes[i] == 'L':
                left[i] = i
            elif dominoes[i] == 'R':
                right[i] = i
            if i > 0:
                left[i] = left[i - 1]
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'R':
                right[i] = i
            elif dominoes[i] == 'L':
                left[i] = i
            if i < n - 1:
                right[i] = right[i + 1]
        ans = []
        for i in range(n):
            if left[i] == right[i]:
                ans.append('.')
            elif left[i] < right[i]:
                ans.append('R')
            else:
                ans.append('L')
        return ''.join(ans)