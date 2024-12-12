import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # Calculate the number of states a pig can represent
        states = minutesToTest // minutesToDie + 1
        # Calculate the minimum number of pigs needed
        pigs = 0
        while states ** pigs < buckets:
            pigs += 1
        return pigs
import json
import random

def generate_test_cases(num_cases=50, max_buckets=1000, max_time=100):
    """
    Generates test cases for the poorPigs function.

    :param num_cases: Number of test cases to generate.
    :param max_buckets: Maximum number of buckets in a test case.
    :param max_time: Maximum time for minutesToDie and minutesToTest.
    :return: List of test cases with inputs and expected outputs.
    """
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        buckets = random.randint(1, max_buckets)
        minutesToDie = random.randint(1, max_time)
        minutesToTest = random.randint(minutesToDie, max_time)

        # Calculate the expected output using the provided solution
        expected_output = solution.poorPigs(buckets, minutesToDie, minutesToTest)

        # Add test case
        test_cases.append({
            "input": {"buckets": buckets, "minutesToDie": minutesToDie, "minutesToTest": minutesToTest},
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_458.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=50, max_buckets=100, max_time=50)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
