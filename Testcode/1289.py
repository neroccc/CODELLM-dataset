import json
import random
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n, res = len(grid), float('inf')
        dp = [[-1] * n for _ in range(n)]

        for j in range(n):
            dp[0][j] = grid[0][j]

        for i in range(1, n):
            for j in range(n):
                temp = float('inf')

                for k in range(n):
                    if j != k:
                        temp = min(temp, grid[i][j] + dp[i - 1][k])

                dp[i][j] = temp

        for j in range(n):
            res = min(res, dp[n - 1][j])

        return res


def generate_random_matrix(size_min=1, size_max=200, value_min=-99, value_max=99):
    """Generate a random square matrix with dimensions and values within given ranges."""
    size = random.randint(size_min, size_max)
    return [[random.randint(value_min, value_max) for _ in range(size)] for _ in range(size)]


def generate_test_cases(num_cases=50, max_size=50):
    """Generate test cases for the Minimum Falling Path Sum with Non-Zero Shifts problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        grid = generate_random_matrix(1, max_size)
        expected_output = solution.minFallingPathSum(grid)
        test_cases.append({"input": grid, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {
            "input": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "output": solution.minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        },
        {
            "input": [[7]],
            "output": solution.minFallingPathSum([[7]])
        },
        {
            "input": [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],
            "output": solution.minFallingPathSum([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]])
        },
    ]
    test_cases.extend(predefined_cases)

    return test_cases


def save_test_cases(filename, test_cases):
    """Save test cases to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(test_cases, f, indent=4)


# Generate and save test cases
if __name__ == "__main__":
    num_cases = 100
    max_size = 50  # Default capped at 50 for faster generation
    test_cases = generate_test_cases(num_cases, max_size)
    save_test_cases("test_cases_1289.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'min_falling_path_sum_test_cases.json'.")
