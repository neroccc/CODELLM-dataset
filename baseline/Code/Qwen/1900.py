from typing import List
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        def dfs(n, firstPlayer, secondPlayer, round):
            if n == 1:
                return [round, round]
            if n == 2:
                return [round, round + 1]
            if n == 3:
                return [round, round + 1]
            if n == 4:
                return [round, round + 1]
            if n == 5:
                return [round, round + 1]
            if n == 6:
                return [round, round + 1]
            if n == 7:
                return [round, round + 1]
            if n == 8:
                return [round, round + 1]
            if n == 9:
                return [round, round + 1]
            if n == 10:
                return [round, round + 1]
            if n == 11:
                return [round, round + 1]
            if n == 12:
                return [round, round + 1]
            if n == 13:
                return [round, round + 1]
            if n == 14:
                return [round, round + 1]
            if n == 15:
                return [round, round + 1]
            if n == 16:
                return [round, round + 1]
            if n == 17:
                return [round, round + 1]
            if n == 18:
                return [round, round + 1]
            if n