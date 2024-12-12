import json
import random
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        nums.sort()
        dp = [0] * len(nums)

        for i, num in enumerate(nums):
            maxSubsetSize = 0
            for k in range(0, i):
                if nums[i] % nums[k] == 0:
                    maxSubsetSize = max(maxSubsetSize, dp[k])
            dp[i] = maxSubsetSize + 1

        maxSize, maxSizeIndex = max([(v, i) for i, v in enumerate(dp)])
        ret = []

        currSize, currTail = maxSize, nums[maxSizeIndex]
        for i in range(maxSizeIndex, -1, -1):
            if currSize == dp[i] and currTail % nums[i] == 0:
                ret.append(nums[i])
                currSize -= 1
                currTail = nums[i]

        return list(reversed(ret))

def generate_random_nums(length: int, value_range=(1, 10**6)) -> List[int]:
    """
    Generates a random list of distinct positive integers.

    :param length: Number of integers to generate.
    :param value_range: Range of values for the integers.
    :return: List of random integers.
    """
    return random.sample(range(value_range[0], value_range[1]), length)

def generate_test_cases(num_cases=100, max_length=1000, value_range=(1, 10**9)):
    """
    Generates test cases for the largestDivisibleSubset function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the nums list.
    :param value_range: Range of values for integers in nums.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize the length of the nums list
        length = random.randint(1, max_length)
        nums = generate_random_nums(length, value_range)

        # Calculate the expected output using the provided solution
        expected_output = solution.largestDivisibleSubset(nums)

        # Add test case
        test_cases.append({
            "input": nums,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_368.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_length=20, value_range=(1, 100))

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
