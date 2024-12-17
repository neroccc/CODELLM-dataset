from typing import List
class Solution:
    def maxNumberOfGroups(self, batchSize: int, groups: List[int]) -> int:
        groups.sort()
        i = 0
        j = len(groups) - 1
        count = 0
        while i <= j:
            if groups[i] + groups[j] < batchSize:
                i += 1
            else:
                j -= 1
                count += 1
        return count
