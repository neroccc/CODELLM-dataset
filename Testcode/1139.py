import json
import random
from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        height = len(grid)
        dp = [[(0, 0)] * width for _ in range(height)]
        max_len = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    dp[i][j] == (0, 0)
                else:
                    if max_len == 0:
                        max_len = 1
                    if i == 0 and j == 0:
                        dp[i][j] = (1, 1)
                    elif i == 0:
                        dp[i][j] = (1, dp[i][j - 1][1] + 1)
                    elif j == 0:
                        dp[i][j] = (dp[i - 1][j][0] + 1, 1)
                    else:
                        dp[i][j] = (dp[i - 1][j][0] + 1, dp[i][j - 1][1] + 1)  # height and width
                        for k in range(max_len, min(dp[i][j])):
                            if dp[i - k][j][1] >= k + 1 and dp[i][j - k][0] >= k + 1:
                                max_len = k + 1
        return max_len * max_len


def generate_random_grid(min_size=1, max_size=100):
    """Generate a random 2D grid of 0s and 1s."""
    rows = random.randint(min_size, max_size)
    cols = random.randint(min_size, max_size)
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]


def generate_test_cases(num_cases=50, max_size=100):
    """Generate test cases for the Largest 1-Bordered Square problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        grid = generate_random_grid(1, max_size)
        expected_output = solution.largest1BorderedSquare(grid)
        test_cases.append({"input": grid, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": [[1, 1, 1], [1, 0, 1], [1, 1, 1]], "output": solution.largest1BorderedSquare([[1, 1, 1], [1, 0, 1], [1, 1, 1]])},
        {"input": [[1, 1, 0, 0]], "output": solution.largest1BorderedSquare([[1, 1, 0, 0]])},
        {"input": [[1]], "output": solution.largest1BorderedSquare([[1]])},
        {"input": [[0]], "output": solution.largest1BorderedSquare([[0]])},
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
    max_size = 100
    test_cases = generate_test_cases(num_cases, max_size)
    save_test_cases("test_cases_1139.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'largest_1_bordered_square_test_cases.json'.")
