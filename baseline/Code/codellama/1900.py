from typing import List
class Solution:
    def getWinner(self, n: int, firstPlayer: int, secondPlayer: int) -> int:
        if n % 2 == 0:
            return