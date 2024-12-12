import json
import random
from typing import List


class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        total_zeros = 0  # number of subsequences of 0s so far
        total_ones = 0  # the number of subsequences of 0s followed by 1s so far
        total_twos = 0  # the number of special subsequences so far

        M = 1000000007

        for n in nums:
            if n == 0:
                # if we have found new 0 we can add it to any existing subsequence of 0s
                # or use only this 0
                total_zeros = (total_zeros + total_zeros + 1) % M
            elif n == 1:
                # if we have found new 1 we can add it to any existing subsequence of 0s or 0s and 1s
                # to get a valid subsequence of 0s and 1s
                total_ones = (total_ones + total_zeros + total_ones) % M
            else:
                # if we have found new 2 we can add it to any existing subsequence of 0s and 1s or 0s,1s and 2s
                # to get a valid subsequence of 0s,1s and 2s
                total_twos = (total_twos + total_ones + total_twos) % M

        return total_twos % M


def generate_test_cases(num_cases=100, max_length=10 ** 5):
    """Generate random test cases for the problem."""
    test_cases = []
    for _ in range(num_cases):
        length = random.randint(1, min(1000, max_length))  # Limit length for practical reasons
        nums = [random.randint(0, 2) for _ in range(length)]
        test_cases.append(nums)
    return test_cases


def compute_expected_outputs(test_cases):
    """Compute the expected outputs for the test cases."""
    solution = Solution()
    outputs = []
    for nums in test_cases:
        output = solution.countSpecialSubsequences(nums)
        outputs.append(output)
    return outputs


# Generate test cases
test_cases = generate_test_cases(num_cases=100)

# Compute expected outputs
expected_outputs = compute_expected_outputs(test_cases)

# Save test cases and outputs to a JSON file
test_data = [{"input": nums, "output": output} for nums, output in zip(test_cases, expected_outputs)]

with open("test_cases_1955.json", "w") as f:
    json.dump(test_data, f, indent=4)

print("Test cases generated and saved to 'test_case_.json'")
