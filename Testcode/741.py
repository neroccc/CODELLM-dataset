import json
import random
from typing import List
from functools import cache


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        bad = float('-inf')

        @cache
        def dfs(k: int, r1: int, r2: int):
            if r1 < 0 or r2 < 0 or r1 >= len(grid) or r2 >= len(grid):
                return bad

            c1 = k - r1
            c2 = k - r2

            if c1 < 0 or c2 < 0 or c1 >= len(grid) or c2 >= len(grid):
                return bad

            if grid[r1][c1] < 0 or grid[r2][c2] < 0:
                return bad

            if k == 0:
                return grid[0][0]  # First step, both paths at (0, 0)

            prev = max(
                dfs(k - 1, r1, r2),  # Down-Down
                dfs(k - 1, r1 - 1, r2),  # Down-Up
                dfs(k - 1, r1, r2 - 1),  # Up-Down
                dfs(k - 1, r1 - 1, r2 - 1)  # Up-Up
            )

            if r1 == r2:
                return prev + grid[r1][c1]
            else:
                return prev + grid[r1][c1] + grid[r2][c2]

        N = len(grid)
        return max(dfs(2 * N - 2, N - 1, N - 1), 0)


def generate_test_cases(num_cases=10):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random grid size between 1 and 50
        n = random.randint(1, 50)
        # Generate a random grid with values -1, 0, and 1
        grid = [[random.choice([-1, 0, 1]) for _ in range(n)] for _ in range(n)]
        # Ensure (0, 0) and (n-1, n-1) are not blocked
        grid[0][0] = random.choice([0, 1])
        grid[n - 1][n - 1] = random.choice([0, 1])
        # Compute the output using the solution's method
        output = solution.cherryPickup(grid)
        # Append the test case
        test_cases.append({
            "input": {
                "grid": grid
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_741.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
