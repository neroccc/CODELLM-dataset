from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            x, y = stones.pop(), stones.pop()
            if x != y:
                stones.append(y - x)
        return stones[0] if stones else 0