import json
import random
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

def generate_random_array(length: int, value_range=(-10**4, 10**4)) -> List[int]:
    """
    Generates a random array of integers.

    :param length: Length of the array.
    :param value_range: Range of values for elements in the array.
    :return: Random integer array.
    """
    return [random.randint(value_range[0], value_range[1]) for _ in range(length)]

def generate_test_cases(num_cases=100, max_length=2500, value_range=(-10**4, 10**4)):
    """
    Generates test cases for the lengthOfLIS function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the input array.
    :param value_range: Range of values for array elements.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize the length of the array
        length = random.randint(1, max_length)
        nums = generate_random_array(length, value_range)

        # Calculate the expected output using the provided solution
        expected_output = solution.lengthOfLIS(nums)

        # Add test case
        test_cases.append({
            "input": nums,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_300.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_length=100, value_range=(-10**4, 10**4))

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
