from typing import List
class Solution:
    def numberOfDuplicateInRange(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            if len(str(i)) != len(set(str(i))):
                count += 1
        return count