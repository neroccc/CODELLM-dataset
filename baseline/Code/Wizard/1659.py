from typing import List
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        def get_happiness(x, y, is_introvert):
            happiness = 120 if is_introvert else 40
            neighbors = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    neighbors += 1
                    happiness -= 30 if is_introvert else 20
            return happiness

        def dfs(x, y, introverts_left, extroverts_left, happiness):
            if x == m and y == n: