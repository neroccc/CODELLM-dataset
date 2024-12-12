from typing import List
import json
import random

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]
def generate_test_cases(num_cases=100, max_nums=50, max_target=1000):
    """
    Generates test cases for the combinationSum4 function.

    :param num_cases: Number of test cases to generate.
    :param max_nums: Maximum number of integers in the nums array.
    :param max_target: Maximum value for the target integer.
    :return: List of test cases with inputs and expected outputs.
    """
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Randomize the length of nums and target
        nums_length = random.randint(1, max_nums)
        nums = random.sample(range(1, 1001), nums_length)  # Ensure unique integers
        target = random.randint(1, max_target)

        # Calculate the expected output using the provided solution
        expected_output = solution.combinationSum4(nums, target)

        # Add test case
        test_cases.append({
            "input": {"nums": nums, "target": target},
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_377.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_nums=20, max_target=200)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
