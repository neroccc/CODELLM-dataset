import json
import random
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max(max_so_far * curr, min_so_far * curr))
            min_so_far = min(curr, min(max_so_far * curr, min_so_far * curr))
            max_so_far = temp_max
            result = max(max_so_far, result)

        return result

def generate_test_cases(num_cases=100, max_length=20000, value_range=(-10, 10)):
    """
    Generates test cases for the maxProduct function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the array.
    :param value_range: Range of values for array elements.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize the length of the nums array
        length = random.randint(1, min(100, max_length))  # Limit length for practical testing
        nums = [random.randint(value_range[0], value_range[1]) for _ in range(length)]

        # Calculate the expected output using the provided solution
        expected_output = solution.maxProduct(nums)

        # Add test case
        test_cases.append({
            "input": nums,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_152.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_length=200, value_range=(-10, 10))

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
