import json
import random
import math
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_row = triangle[0]
        for row in range(1, len(triangle)):
            curr_row = []
            for col in range(row + 1):
                smallest_above = math.inf
                if col > 0:
                    smallest_above = prev_row[col - 1]
                if col < row:
                    smallest_above = min(smallest_above, prev_row[col])
                curr_row.append(triangle[row][col] + smallest_above)
            prev_row = curr_row
        return min(prev_row)

def generate_random_triangle(max_rows=200, value_range=(-10**4, 10**4)):
    """
    Generates a random triangle array.

    :param max_rows: Maximum number of rows in the triangle.
    :param value_range: Range of values for the elements in the triangle.
    :return: Random triangle array.
    """
    rows = random.randint(1, max_rows)
    triangle = [[random.randint(*value_range) for _ in range(row + 1)] for row in range(rows)]
    return triangle

def generate_test_cases(num_cases=1000, max_rows=200, value_range=(-10**4, 10**4)):
    """
    Generates test cases for the minimumTotal function.

    :param num_cases: Number of test cases to generate.
    :param max_rows: Maximum number of rows in the triangle.
    :param value_range: Range of values for the elements in the triangle.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        triangle = generate_random_triangle(max_rows=max_rows, value_range=value_range)
        expected_output = solution.minimumTotal(triangle)
        test_cases.append({
            "input": triangle,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_120.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_rows=200, value_range=(-10**4, 10**4))

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
