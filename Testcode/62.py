import json
import random
from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)

def generate_test_cases(num_cases=1000, max_m=100, max_n=100):
    """
    Generates test cases for the uniquePaths function.

    :param num_cases: Number of test cases to generate.
    :param max_m: Maximum value of m (grid rows).
    :param max_n: Maximum value of n (grid columns).
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize the values of m and n
        m = random.randint(1, max_m)
        n = random.randint(1, max_n)

        # Calculate the expected output using the provided solution
        expected_output = solution.uniquePaths(m, n)

        # Add test case
        test_cases.append({
            "input": {"m": m, "n": n},
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_62.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    num_cases = 1000
    test_cases = generate_test_cases(num_cases=num_cases, max_m=100, max_n=100)

    # Save to file
    save_test_cases_to_file(test_cases)
    print(f"{num_cases} test cases saved to 'test_case_.json'.")
