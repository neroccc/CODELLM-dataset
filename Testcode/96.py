import json

class Solution:
    def numTrees(self, n: int) -> int:
        C = 1
        for i in range(0, n):
            C = C * 2 * (2 * i + 1) / (i + 2)
        return int(C)

def generate_test_cases(max_n=19):
    """
    Generates test cases for the numTrees function.

    :param max_n: Maximum value of n (1 to max_n).
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for n in range(1, max_n + 1):
        # Calculate the expected output using the provided solution
        expected_output = solution.numTrees(n)

        # Add test case
        test_cases.append({
            "input": n,
            "output": expected_output
        })
    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_96.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(max_n=19)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
