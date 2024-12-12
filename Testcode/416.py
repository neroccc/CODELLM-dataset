from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Calculate the sum of array elements
        total_sum = sum(nums)

        # If total_sum is odd, it's not possible to partition
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)

        # Create a DP table with dimensions (n+1) x (subset_sum+1)
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]

        # Base case: A subset with sum 0 is always possible
        dp[0][0] = True

        # Populate the DP table
        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(subset_sum + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]

        # Return whether it's possible to partition into subsets with equal sum
        return dp[n][subset_sum]

import json
import random

def generate_test_cases(num_cases=100, max_length=50, max_value=100):
    """
    Generates test cases for the canPartition function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the array.
    :param max_value: Maximum value of elements in the array.
    :return: List of test cases with inputs and expected outputs.
    """
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        length = random.randint(1, max_length)
        nums = [random.randint(1, max_value) for _ in range(length)]

        # Calculate the expected output using the provided solution
        expected_output = solution.canPartition(nums)

        # Add test case
        test_cases.append({
            "input": nums,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_416.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_length=30, max_value=50)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
