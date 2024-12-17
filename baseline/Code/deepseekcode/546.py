from typing import List
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        dp = [[[0]*100 for _ in range(100)] for _ in range(100)]
        def solve(l, r, k):
            if l > r: return 0
            if dp[l][r][k] != 0: return dp[l][r][k]
            while (r > l) and (boxes[r] == boxes[r - 1]):
                r -= 1
                k += 1
            res = solve(l, r - 1, 0) + (k + 1) * (k + 1)
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, solve(l, i, k + 1) + solve(i + 1, r - 1, 0))
            dp[l][r][k] = res
            return res
        return solve(0, len(boxes) - 1, 0)