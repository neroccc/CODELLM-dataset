import json
import random
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        dp = [[[0] * (cols + 2) for _ in range(cols + 2)] for _ in range(rows + 1)]

        def get_next_max(row, col_r1, col_r2):
            res = 0
            for next_col_r1 in (col_r1 - 1, col_r1, col_r1 + 1):
                for next_col_r2 in (col_r2 - 1, col_r2, col_r2 + 1):
                    res = max(res, dp[row + 1][next_col_r1 + 1][next_col_r2 + 1])

            return res

        for row in reversed(range(rows)):
            for col_r1 in range(min(cols, row + 2)):
                for col_r2 in range(max(0, cols - row - 1), cols):
                    reward = grid[row][col_r1] + grid[row][col_r2]
                    if col_r1 == col_r2:
                        reward //= 2  # Use integer division to avoid float

                    dp[row][col_r1 + 1][col_r2 + 1] = reward + get_next_max(row, col_r1, col_r2)

        return dp[0][1][cols]


# Helper function to generate random grids
def generate_grid(rows, cols):
    return [[random.randint(0, 100) for _ in range(cols)] for _ in range(rows)]


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        rows = random.randint(2, 70)
        cols = random.randint(2, 70)
        grid = generate_grid(rows, cols)

        # Compute the expected output using the provided solution
        expected_output = solution.cherryPickup(grid)

        test_cases.append({
            "input": {"grid": grid},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1463.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
