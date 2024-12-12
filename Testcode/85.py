import json
import random
from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n  # initialize left as the leftmost boundary possible
        right = [n] * n  # initialize right as the rightmost boundary possible
        height = [0] * n

        maxarea = 0

        for i in range(m):
            cur_left, cur_right = 0, n
            # update height
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            # update left
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update right
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update the area
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))

        return maxarea

def generate_test_cases(num_cases=1000, max_rows=200, max_cols=200):
    """
    Generates test cases for the maximalRectangle function.

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
        matrix = [[random.choice(["0", "1"]) for _ in range(cols)] for _ in range(rows)]

        # Calculate the expected output using the provided solution
        expected_output = solution.maximalRectangle(matrix)

        # Add test case
        test_cases.append({
            "input": matrix,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_85.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    num_cases = 100
    test_cases = generate_test_cases(num_cases=num_cases, max_rows=200, max_cols=200)

    # Save to file
    save_test_cases_to_file(test_cases)
    print(f"{num_cases} test cases saved to 'test_case_.json'.")
