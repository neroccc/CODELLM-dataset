from typing import List
class Solution:
    def grayCode(self, n: int, start: int) -> List[int]:
        if n == 0:
            return [start]
        res = [start]
        for i in range(n - 1):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] | (1 << i))
        return res
