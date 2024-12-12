import json
import random
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for num in sorted(nums):
            for i in dp[:]:
                dp[(i + num) % 3] = max(dp[(i + num) % 3], i + num)
        return dp[0]


def generate_random_array(min_length=1, max_length=10**4, min_value=1, max_value=10**4):
    """Generate a random array of integers."""
    length = random.randint(min_length, max_length)
    return [random.randint(min_value, max_value) for _ in range(length)]


def generate_test_cases(num_cases=50, max_length=1000):
    """Generate test cases for the Maximum Sum Divisible by Three problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        nums = generate_random_array(1, max_length)
        expected_output = solution.maxSumDivThree(nums)
        test_cases.append({"input": nums, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": [3, 6, 5, 1, 8], "output": solution.maxSumDivThree([3, 6, 5, 1, 8])},
        {"input": [4], "output": solution.maxSumDivThree([4])},
        {"input": [1, 2, 3, 4, 4], "output": solution.maxSumDivThree([1, 2, 3, 4, 4])},
        {"input": [10, 11, 12, 13], "output": solution.maxSumDivThree([10, 11, 12, 13])},
        {"input": [1, 1, 1], "output": solution.maxSumDivThree([1, 1, 1])},
    ]
    test_cases.extend(predefined_cases)

    return test_cases


def save_test_cases(filename, test_cases):
    """Save test cases to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(test_cases, f, indent=4)


# Generate and save test cases
if __name__ == "__main__":
    num_cases = 100
    max_length = 1000  # Default capped at 1000 for faster generation
    test_cases = generate_test_cases(num_cases, max_length)
    save_test_cases("../test_cases_1062.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'max_sum_divisible_by_three_test_cases.json'.")
