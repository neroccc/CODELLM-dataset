from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total_count = 0
        # Create a list of dictionaries to store counts of differences
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                # Increment the count of subsequences ending at i with this difference
                dp[i][diff] += 1
                # If there are subsequences ending at j with this difference, extend them
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    total_count += dp[j][diff]

        return total_count

import json
import random

def generate_test_cases(num_cases=100, max_length=10, value_range=(-1000, 1000)):
    """
    Generates test cases for the numberOfArithmeticSlices function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the array.
    :param value_range: Range of values for the array elements.
    :return: List of test cases with inputs and expected outputs.
    """
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        length = random.randint(3, max_length)  # At least 3 elements for valid subsequences
        nums = [random.randint(*value_range) for _ in range(length)]

        # Calculate the expected output using the provided solution
        expected_output = solution.numberOfArithmeticSlices(nums)

        # Add test case
        test_cases.append({
            "input": nums,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_446.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=50, max_length=20, value_range=(-10, 10))

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
