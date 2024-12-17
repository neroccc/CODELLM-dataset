from typing import List
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        return sum(max(target[i] - (target[i - 1] if i > 0 else 0), 0) for i in range(len(target)))