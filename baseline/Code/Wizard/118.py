from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i // 2 + 1):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
                row[-j - 1] = row[j]
            res.append(row)
        return res