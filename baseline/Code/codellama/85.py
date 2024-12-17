from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        heights = [0] * m
        ans = 0

        def largestRectangleArea(heights: List[int]) -> int:
            n = len(heights)
            stack = [-1]
            ans = 0

            for i in range(n):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    height = heights[stack.pop()]
                    width = i - stack[-1] - 1
                    ans = max(ans, height * width)
                stack.append(i)

            while stack[-1] != -1:
                height = heights[stack.pop()]
                width = n - stack[-1] - 1
                ans = max(ans, height * width)

            return ans

        for i in range(n):
            for j in range(m):
                heights[j] = heights[j] + 1 if matrix[i][j] == "1" else 0
            ans = max(ans, largestRectangleArea(heights))

        return ans

