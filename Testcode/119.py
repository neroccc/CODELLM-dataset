import json

class Solution:
    def getRow(self, n):
        row = [1]
        for k in range(1, n + 1):
            row.append(int((row[-1] * (n - k + 1)) / k))
        return row

def generate_test_cases(max_row_index=33):
    """
    Generates test cases for the getRow function.

    :param max_row_index: Maximum value of rowIndex (0 to max_row_index).
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for rowIndex in range(max_row_index + 1):
        # Calculate the expected output using the provided solution
        expected_output = solution.getRow(rowIndex)

        # Add test case
        test_cases.append({
            "input": rowIndex,
            "output": expected_output
        })
    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_119.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(max_row_index=33)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
