import math
from typing import List
class Solution:
    def twoEggDrop(self, n: int) -> int:
        return int(math.ceil((math.sqrt(8 * n + 1) - 1) / 2))