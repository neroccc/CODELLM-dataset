from itertools import combinations
from typing import List
class Solution:
    def get_kth_instructions(self, destination: List[int], k: int) -> str:
        row, col = destination
        n = row + col
        instructions = []

        for combo in combinations(["H", "V"], n):
            s = "".join(combo)
            if s.count("H") == row and s.count("V") == col:
                instructions.append(s)

        instructions.sort()
        return instructions[k - 1]