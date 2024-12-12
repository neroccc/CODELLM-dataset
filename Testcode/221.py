import json
import random
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        dp = [0] * (cols + 1)
        maxsqlen = 0
        prev = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == "1":
                    dp[j] = min(min(dp[j - 1], prev), dp[j]) + 1
                    maxsqlen = max(maxsqlen, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return maxsqlen * maxsqlen

def generate_random_binary_matrix(rows: int, cols: int) -> List[List[str]]:
    """
    Generates a random binary matrix of given dimensions.

    :param rows: Number of rows in the matrix.
    :param cols: Number of columns in the matrix.
    :return: Random binary matrix.
    """
    return [[random.choice(["0", "1"]) for _ in range(cols)] for _ in range(rows)]

def generate_test_cases(num_cases=100, max_rows=300, max_cols=300):
    """
    Generates test cases for the maximalSquare function.

    :param num_cases: Number of test cases to generate.
    :param max_rows: Maximum number of rows in the matrix.
    :param max_cols: Maximum number of columns in the matrix.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        rows = random.randint(1, max_rows)
        cols = random.randint(1, max_cols)
        matrix = generate_random_binary_matrix(rows, cols)

        # Calculate the expected output using the provided solution
        expected_output = solution.maximalSquare(matrix)

        # Add test case
        test_cases.append({
            "input": matrix,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_221.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_rows=50, max_cols=50)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
