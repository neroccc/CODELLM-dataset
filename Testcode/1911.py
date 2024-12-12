import json
import random
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]  # initialize dp
        dp[0][0] = nums[0]  # pre-define
        dp[0][1] = 0  # pre-define

        for i in range(1, n):  # iterate through nums starting from index 1
            dp[i][0] = max(nums[i] + dp[i - 1][1], dp[i - 1][
                0])  # find which value is higher between choosing or not choosing when the last value is plus.
            dp[i][1] = max(-nums[i] + dp[i - 1][0], dp[i - 1][
                1])  # find which value is higher between choosing or not choosing when the last value is minus.

        return max(dp[
                       -1])  # find the maximum of the last array of dp of whether the last value is plus or minus, this will be our answer.


def generate_test_cases(num_cases=100, max_length=10 ** 5, max_value=10 ** 5):
    """Generate a list of test cases with random inputs."""
    test_cases = []
    for _ in range(num_cases):
        length = random.randint(1, min(100, max_length))  # Limit length for practicality
        nums = [random.randint(1, max_value) for _ in range(length)]
        test_cases.append(nums)
    return test_cases


def compute_expected_outputs(test_cases):
    """Compute the expected outputs for a list of test cases."""
    solution = Solution()
    outputs = []
    for nums in test_cases:
        output = solution.maxAlternatingSum(nums)
        outputs.append(output)
    return outputs


# Generate test cases
test_cases = generate_test_cases(num_cases=100, max_length=1000, max_value=1000)

# Compute expected outputs
expected_outputs = compute_expected_outputs(test_cases)

# Save test cases and outputs to a JSON file
test_data = [{"input": nums, "output": output} for nums, output in zip(test_cases, expected_outputs)]

with open("test_cases_1911.json", "w") as f:
    json.dump(test_data, f, indent=4)

print("Test cases generated and saved to 'test_case_.json'")
