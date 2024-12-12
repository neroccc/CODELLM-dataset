from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        dp = [0] * n  # dp[i] stores the number of arithmetic slices ending at index i
        total_slices = 0

        for i in range(2, n):
            # Check if the current triplet forms an arithmetic sequence
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
                total_slices += dp[i]

        return total_slices


import json
import random

def generate_random_array(length, value_range=(-1000, 1000)):
    """
    Generates a random array of integers.

    :param length: Number of elements in the array.
    :param value_range: Range of integer values for the array.
    :return: List of random integers.
    """
    return [random.randint(value_range[0], value_range[1]) for _ in range(length)]

def generate_test_cases(num_cases=100, max_length=50, value_range=(-1000, 1000)):
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
        length = random.randint(1, max_length)
        nums = generate_random_array(length, value_range)

        # Calculate the expected output using the provided solution
        expected_output = solution.numberOfArithmeticSlices(nums)

        # Add test case
        test_cases.append({
            "input": nums,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_413.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_length=20, value_range=(-50, 50))

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
