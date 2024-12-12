import json
import random
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Special handling for empty case.
        if not nums:
            return 0

        N = len(nums)

        rob_next_plus_one = 0
        rob_next = nums[N - 1]

        # DP table calculations.
        for i in range(N - 2, -1, -1):
            # Same as recursive solution.
            current = max(rob_next, rob_next_plus_one + nums[i])

            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current

        return rob_next

def generate_random_houses(length: int, value_range=(0, 400)) -> List[int]:
    """
    Generates a random list of house values.

    :param length: Number of houses.
    :param value_range: Range of values for each house.
    :return: List of random house values.
    """
    return [random.randint(value_range[0], value_range[1]) for _ in range(length)]

def generate_test_cases(num_cases=100, max_length=100, value_range=(0, 400)):
    """
    Generates test cases for the rob function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum number of houses.
    :param value_range: Range of values for each house.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize the number of houses
        length = random.randint(1, max_length)
        houses = generate_random_houses(length, value_range)

        # Calculate the expected output using the provided solution
        expected_output = solution.rob(houses)

        # Add test case
        test_cases.append({
            "input": houses,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_198.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_length=100, value_range=(0, 400))

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
