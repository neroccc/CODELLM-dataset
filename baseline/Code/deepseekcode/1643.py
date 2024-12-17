from typing import List
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        nCr = [[0 for _ in range(31)] for _ in range(31)]
        for i in range(0, 31):
            nCr[i][0] = 1
            for j in range(1, i+1):
                nCr[i][j] = nCr[i-1][j-1] + nCr[i-1][j]
        
        v, h = destination
        ans = []
        for _ in range(h + v):
            if h == 0:
                ans.append('V')
                v -= 1
            elif v == 0:
                ans.append('H')
                h -= 1
            elif nCr[h + v - 1][h - 1] < k:
                ans.append('V')
                v -= 1
                k -= nCr[h + v][h]
            else:
                ans.append('H')
                h -= 1
        return "".join(ans)