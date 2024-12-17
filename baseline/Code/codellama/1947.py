from typing import List
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        n = len(students)
        m = len(students[0])
        dp = [[0] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = 0
        for mask in range(1, 1 << n):
            for i in range(n):
                if mask & (1 << i):