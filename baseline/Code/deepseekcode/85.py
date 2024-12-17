from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        ans = 0

        for i in range(m):
            stack = [-1]
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
                while stack and heights[stack[-1]] > heights[j]:
                    h = heights[stack.pop()]
                    w = j - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(j)
        return ans