import json
import random
from math import comb
from typing import List


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def f(nums):
            if len(nums) <= 2:
                return 1
            left = [v for v in nums if v < nums[0]]
            right = [v for v in nums if v > nums[0]]
            return comb(len(left) + len(right), len(right)) * f(left) * f(right)

        return (f(nums) - 1) % (10 ** 9 + 7)


# Helper function to generate random permutations
def generate_random_permutation(length):
    return random.sample(range(1, length + 1), length)


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        length = random.randint(1, 1000)
        nums = generate_random_permutation(length)

        # Compute expected output using the provided solution
        expected_output = solution.numOfWays(nums)

        test_cases.append({
            "input": {"nums": nums},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1569.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
