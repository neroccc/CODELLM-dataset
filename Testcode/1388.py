import json
import random
from typing import List
from functools import lru_cache


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        @lru_cache(None)
        def fn(i, k, first):
            """Return max sum of k pieces from slices[i:]."""
            if k == 0: return 0
            if i >= len(slices) or first and i == len(slices) - 1: return float('-inf')
            if i == 0: return max(fn(i + 1, k, False), slices[i] + fn(i + 2, k - 1, True))
            return max(fn(i + 1, k, first), slices[i] + fn(i + 2, k - 1, first))

        return fn(0, len(slices) // 3, None)


# Generate test cases
def generate_test_cases(num_cases=100):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Randomly decide the number of slices (must be a multiple of 3)
        num_slices = random.randint(1, 166) * 3
        # Generate random slice sizes
        slices = [random.randint(1, 1000) for _ in range(num_slices)]
        # Compute the expected output using the solution
        expected_output = solution.maxSizeSlices(slices)
        # Add the test case to the list
        test_cases.append({"slices": slices, "output": expected_output})

    # Save the test cases to a file
    with open("test_cases_1388.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate 100 test cases
generate_test_cases()
