import json
import random
from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        max_len = 1
        last_wiggle = None

        for i in range(1, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and last_wiggle != 1) or (diff < 0 and last_wiggle != -1):
                max_len += 1
                last_wiggle = 1 if diff > 0 else -1

        return max_len

def generate_random_nums(length: int, value_range=(0, 1000)) -> List[int]:
    """
    Generates a random list of integers.

    :param length: Number of integers to generate.
    :param value_range: Range of values for the integers.
    :return: List of random integers.
    """
    return [random.randint(value_range[0], value_range[1]) for _ in range(length)]

def generate_test_cases(num_cases=100, max_length=1000, value_range=(0, 1000)):
    """
    Generates test cases for the wiggleMaxLength function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the nums list.
    :param value_range: Range of values for integers in nums.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize the length of the nums list
        length = random.randint(1, max_length)
        nums = generate_random_nums(length, value_range)

        # Calculate the expected output using the provided solution
        expected_output = solution.wiggleMaxLength(nums)

        # Add test case
        test_cases.append({
            "input": nums,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_376.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_length=100, value_range=(0, 1000))

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
