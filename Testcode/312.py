import json
import random
from typing import List
from functools import lru_cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Special case
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        # Handle edge case
        nums = [1] + nums + [1]

        @lru_cache(None)  # memoization
        def dp(left, right):
            if right - left < 0:
                return 0
            result = 0
            for i in range(left, right + 1):
                gain = nums[left - 1] * nums[i] * nums[right + 1]
                remaining = dp(left, i - 1) + dp(i + 1, right)
                result = max(result, remaining + gain)
            return result

        return dp(1, len(nums) - 2)

def generate_random_array(length: int, value_range=(0, 100)) -> List[int]:
    """
    Generates a random array of integers.

    :param length: Length of the array.
    :param value_range: Range of values for elements in the array.
    :return: Random integer array.
    """
    return [random.randint(value_range[0], value_range[1]) for _ in range(length)]

def generate_test_cases(num_cases=100, max_length=300, value_range=(0, 100)):
    """
    Generates test cases for the maxCoins function.

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
        expected_output = solution.maxCoins(nums)

        # Add test case
        test_cases.append({
            "input": nums,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_312.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_length=10, value_range=(0, 10))

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
