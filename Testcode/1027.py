import json
import random
from typing import List

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i, a2 in enumerate(A[1:], start=1):
            for j, a1 in enumerate(A[:i]):
                d = a2 - a1
                if (j, d) in dp:
                    dp[i, d] = dp[j, d] + 1
                else:
                    dp[i, d] = 2
        return max(dp.values())


def generate_random_array(max_length=1000, max_value=500):
    """Generate a random array of integers for the test case."""
    length = random.randint(2, max_length)
    return [random.randint(0, max_value) for _ in range(length)]


def generate_test_cases(num_cases=50, max_length=1000, max_value=500):
    """Generate test cases for the Longest Arithmetic Subsequence problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        nums = generate_random_array(max_length, max_value)
        expected_output = solution.longestArithSeqLength(nums)
        test_cases.append({"input": nums, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": [3, 6, 9, 12], "output": solution.longestArithSeqLength([3, 6, 9, 12])},
        {"input": [9, 4, 7, 2, 10], "output": solution.longestArithSeqLength([9, 4, 7, 2, 10])},
        {"input": [20, 1, 15, 3, 10, 5, 8], "output": solution.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8])},
        {"input": [1, 2], "output": solution.longestArithSeqLength([1, 2])},
        {"input": [500] * 1000, "output": solution.longestArithSeqLength([500] * 1000)},
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
    max_value = 500
    test_cases = generate_test_cases(num_cases, max_length, max_value)
    save_test_cases("../test_cases_1027.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'longest_arithmetic_subsequence_test_cases.json'.")
