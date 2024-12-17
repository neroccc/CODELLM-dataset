from collections import deque
from typing import List
class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        remainders = [0] * batchSize
        for group in groups:
            remainders[group % batchSize] += 1

        happy = remainders[0]
        remainders[0] = 0

        queue = deque()
        for i in range(1, batchSize):
            if remainders[i] > 0:
                queue.append(i)

        while queue:
            remainder = queue.popleft()
            for i in range(1, batchSize):
                newRemainder = (remainder + i) % batchSize
                if remainders[newRemainder] > 0:
                    remainders[newRemainder] -= 1
                    if newRemainder == 0:
                        happy += 1
                    else:
                        queue.append(newRemainder)

        return happy