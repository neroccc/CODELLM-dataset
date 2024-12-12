import json
import random
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        rows, cols = len(matrix), len(matrix[0])
        nbr = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def longest_path(r1, c1):
            if (r1, c1) in dp:
                return dp[(r1, c1)]
            max_path = 1
            for dr, dc in nbr:
                nr, nc = r1 + dr, c1 + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[nr][nc] > matrix[r1][c1]:
                        max_path = max(max_path, 1 + longest_path(nr, nc))
            dp[(r1, c1)] = max_path
            return dp[(r1, c1)]

        ans = 1
        for r in range(rows):
            for c in range(cols):
                path_l = longest_path(r, c)
                ans = max(ans, path_l)
        return ans

def generate_random_matrix(rows: int, cols: int, value_range=(0, 2**31 - 1)) -> List[List[int]]:
    """
    Generates a random matrix of integers.

    :param rows: Number of rows in the matrix.
    :param cols: Number of columns in the matrix.
    :param value_range: Range of values for matrix elements.
    :return: Random integer matrix.
    """
    return [[random.randint(value_range[0], value_range[1]) for _ in range(cols)] for _ in range(rows)]

def generate_test_cases(num_cases=100, max_rows=200, max_cols=200, value_range=(0, 1000)):
    """
    Generates test cases for the longestIncreasingPath function.

    :param num_cases: Number of test cases to generate.
    :param max_rows: Maximum number of rows in the matrix.
    :param max_cols: Maximum number of columns in the matrix.
    :param value_range: Range of values for matrix elements.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize the number of rows and columns
        rows = random.randint(1, max_rows)
        cols = random.randint(1, max_cols)
        matrix = generate_random_matrix(rows, cols, value_range)

        # Calculate the expected output using the provided solution
        expected_output = solution.longestIncreasingPath(matrix)

        # Add test case
        test_cases.append({
            "input": matrix,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_329.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_rows=10, max_cols=10, value_range=(0, 100))

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
