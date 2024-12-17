from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        res = [1, 1]
        for i in range(2, rowIndex + 1):
            temp = [1]
            for j in range(1, i):
                temp.append(res[j - 1] + res[j])
            temp.append(1)
            res = temp
        return res