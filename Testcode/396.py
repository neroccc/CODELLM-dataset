from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s, n = sum(nums), len(nums)
        cur_sum = sum(i * num for i, num in enumerate(nums))
        max_value = cur_sum

        for i in range(1, n):
            cur_sum = cur_sum + s - nums[-i] * n
            max_value = max(max_value, cur_sum)

        return max_value
import json
import random

def generate_random_nums(length: int, value_range=(-100, 100)) -> List[int]:
    """
    Generates a random list of integers.

    :param length: Number of integers to generate.
    :param value_range: Range of values for the integers.
    :return: List of random integers.
    """
    return [random.randint(value_range[0], value_range[1]) for _ in range(length)]

def generate_test_cases(num_cases=100, max_length=100, value_range=(-100, 100)):
    """
    Generates test cases for the maxRotateFunction function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the nums array.
    :param value_range: Range of values for integers in nums.
    :return: List of test cases with inputs and expected outputs.
    """
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        length = random.randint(1, max_length)
        nums = generate_random_nums(length, value_range)

        # Calculate the expected output using the provided solution
        expected_output = solution.maxRotateFunction(nums)

        # Add test case
        test_cases.append({
            "input": nums,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_396.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_length=10, value_range=(-10, 10))

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
