from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] + [0]*rowIndex
        for i in range(rowIndex):
            row[rowIndex-i] = row[rowIndex-i] + row[rowIndex-i-1]
        return row