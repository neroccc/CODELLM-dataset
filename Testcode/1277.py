import json
import random
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = matrix[i][j]
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return sum(sum(row) for row in dp)


def generate_random_matrix(max_rows=300, max_cols=300):
    """Generate a random binary matrix with dimensions between 1 and max_rows, max_cols."""
    rows = random.randint(1, max_rows)
    cols = random.randint(1, max_cols)
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]


def generate_test_cases(num_cases=50, max_rows=50, max_cols=50):
    """Generate test cases for the Count Square Submatrices with All Ones problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        matrix = generate_random_matrix(max_rows, max_cols)
        expected_output = solution.countSquares(matrix)
        test_cases.append({"input": matrix, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {
            "input": [
                [0, 1, 1, 1],
                [1, 1, 1, 1],
                [0, 1, 1, 1]
            ],
            "output": solution.countSquares([
                [0, 1, 1, 1],
                [1, 1, 1, 1],
                [0, 1, 1, 1]
            ])
        },
        {
            "input": [
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 0]
            ],
            "output": solution.countSquares([
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 0]
            ])
        },
        {
            "input": [[1]],
            "output": solution.countSquares([[1]])
        },
        {
            "input": [[0]],
            "output": solution.countSquares([[0]])
        },
        {
            "input": [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            "output": solution.countSquares([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
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
    max_rows = 50  # Limit rows and cols for faster generation
    max_cols = 50
    test_cases = generate_test_cases(num_cases, max_rows, max_cols)
    save_test_cases("../test_cases_1277.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'count_squares_test_cases.json'.")
