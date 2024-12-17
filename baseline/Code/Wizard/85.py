from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        max_area = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    dp[i][j] = 1

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "0":
                    continue
                if j == 0 or matrix[i][j - 1] == "0":
                    dp[i][j] = dp[i][j] + dp[i][j - 1] if j > 0 else 1

        for i in range(n):
            stack = []
            for j in range(m + 1):
                while stack and (j == m or dp[i][stack[-1]] > dp[i][j]):
                    height = dp[i][stack.pop()]
                    width = j - 1 - stack[-1] if stack else j
                    max_area = max(max_area, height * width)
                stack.append(j)

        return max_area