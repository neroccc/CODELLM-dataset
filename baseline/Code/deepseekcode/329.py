from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(matrix), len(matrix[0])
        cache = [[-1]*n for _ in range(m)]
        
        def dfs(i, j):
            if cache[i][j] != -1:
                return cache[i][j]
            
            val = matrix[i][j]
            cache[i][j] = 1 + max(
                (dfs(i+di, j+dj) for di, dj in directions if 0<=i+di<m and 0<=j+dj<n and matrix[i+di][j+dj] > val),
                default=0)
            return cache[i][j]
        
        return max(dfs(i, j) for i in range(m) for j in range(n))