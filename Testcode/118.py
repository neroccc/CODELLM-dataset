import json
from typing import List

class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle

def generate_test_cases(max_num_rows=30):
    """
    Generates test cases for the generate function.

    :param max_num_rows: Maximum value of numRows (1 to max_num_rows).
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for num_rows in range(1, max_num_rows + 1):
        # Calculate the expected output using the provided solution
        expected_output = solution.generate(num_rows)

        # Add test case
        test_cases.append({
            "input": num_rows,
            "output": expected_output
        })
    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_118.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(max_num_rows=30)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
