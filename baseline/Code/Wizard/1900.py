from typing import List
class Solution:
    def tournamentRounds(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        if firstPlayer == secondPlayer:
            return [1, 1]

        if firstPlayer > secondPlayer:
            firstPlayer, secondPlayer = secondPlayer, firstPlayer

        firstPlayer -= 1
        secondPlayer -= 1

        first_round = 1
        second_round = 1

        while firstPlayer != secondPlayer:
            if firstPlayer + secondPlayer >= n:
                first_round += 1
                second_round += 1
                firstPlayer //= 2
                secondPlayer //= 2
            else:
                first_round += 1
                secondPlayer //= 2

        return [first_round, second_