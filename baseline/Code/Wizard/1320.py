from typing import List
class Solution:
    def minDistance(self, word: str) -> int:
        coords = {
            'A': (0, 0),
            'B': (0, 1),
            'C': (0, 2),
            'D': (1, 0),
            'E': (1, 1),
            'F': (1, 2),
            'G': (2, 0),
            'H': (2, 1),
            'I': (2, 2),
            'J': (3, 0),
            'K': (3, 1),
            'L': (3, 2),
            'M': (4, 0),
            'N': (4, 1),
            'O': (4, 2),
            'P': (5, 0),
            'Q': (5, 1),
            'R': (5, 2),
            'S': (6, 0),
            'T': (6, 1),
            'U': (6, 2),
            'V': (7, 0),
            'W': (7, 1),
            'X': (7, 2),
            'Y': (8, 0),
            'Z': (8, 1)
        }

        def distance(a, b):
            return abs(coords[a][0] - coords[b][0]) + abs(coords[a][1] - coords[b][1])

        n = len(word)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 0

        for diff in range(1, n):
            for i in range(n - diff):
                j = i + diff
                if word[i] == word[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], d