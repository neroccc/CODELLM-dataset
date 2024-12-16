import json
import random
from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        min_pos = 0
        max_pos = 0
        count = 0

        while max_pos < n:
            for i in range(len(ranges)):
                if i - ranges[i] <= min_pos and i + ranges[i] > max_pos:
                    max_pos = i + ranges[i]

            if max_pos == min_pos:
                return -1

            count += 1
            min_pos = max_pos

        return count


# Generate test cases
def generate_test_cases(num_cases=100):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Randomly decide the size of the garden
        n = random.randint(1, 10 ** 4)
        # Generate random ranges for taps
        ranges = [random.randint(0, 100) for _ in range(n + 1)]
        # Compute the expected output using the solution
        expected_output = solution.minTaps(n, ranges)
        # Add the test case to the list
        test_cases.append({"input":{"n": n, "ranges": ranges}, "output": expected_output})

    # Save the test cases to a file
    with open("../Testcase/test_cases_1326.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate 100 test cases
generate_test_cases()
