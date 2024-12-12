import json
import random
from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        max_len = 0

        for num in arr:
            dp[num] = dp.get(num - difference, 0) + 1
            max_len = max(max_len, dp[num])

        return max_len


def generate_random_array(min_length=1, max_length=10**5, min_value=-10**4, max_value=10**4):
    """Generate a random array of integers."""
    length = random.randint(min_length, max_length)
    return [random.randint(min_value, max_value) for _ in range(length)]


def generate_test_cases(num_cases=50, max_length=1000, min_value=-10**4, max_value=10**4):
    """Generate test cases for the Longest Arithmetic Subsequence of Given Difference problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        arr = generate_random_array(1, max_length, min_value, max_value)
        difference = random.randint(-10**4, 10**4)
        expected_output = solution.longestSubsequence(arr, difference)
        test_cases.append({"input": {"arr": arr, "difference": difference}, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": {"arr": [1, 2, 3, 4], "difference": 1}, "output": solution.longestSubsequence([1, 2, 3, 4], 1)},
        {"input": {"arr": [1, 3, 5, 7], "difference": 1}, "output": solution.longestSubsequence([1, 3, 5, 7], 1)},
        {"input": {"arr": [1, 5, 7, 8, 5, 3, 4, 2, 1], "difference": -2}, "output": solution.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2)},
        {"input": {"arr": [10, 20, 30], "difference": 10}, "output": solution.longestSubsequence([10, 20, 30], 10)},
        {"input": {"arr": [1], "difference": 0}, "output": solution.longestSubsequence([1], 0)},
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
    max_length = 1000
    test_cases = generate_test_cases(num_cases, max_length)
    save_test_cases("../test_cases_1218.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'longest_arithmetic_subsequence_test_cases.json'.")
