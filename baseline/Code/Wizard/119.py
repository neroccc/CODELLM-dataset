from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        row = [1, 1]
        for i in range(2, rowIndex + 1):
            curr = [1]
            for j in range(1, i):
                curr.append(row[j - 1] + row[j])
            curr.append(1)
            row = curr

        return row