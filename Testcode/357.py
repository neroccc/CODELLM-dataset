import json
import random

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def count(k):
            if k == max(10 - n, 0):
                return 0
            return k * (1 + count(k - 1))
        if n == 0:
            return 1
        return 9 * count(9) + 10

def generate_test_cases(num_cases=10, max_n=8):
    """
    Generates test cases for the countNumbersWithUniqueDigits function.

    :param num_cases: Number of test cases to generate.
    :param max_n: Maximum value for n.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize n value within the valid range
        n = random.randint(0, max_n)

        # Calculate the expected output using the provided solution
        expected_output = solution.countNumbersWithUniqueDigits(n)

        # Add test case
        test_cases.append({
            "input": n,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_357.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=10, max_n=8)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
