import json
import random
from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = pos = neg = 0
        for x in nums:
            if x > 0:
                pos, neg = 1 + pos, 1 + neg if neg else 0
            elif x < 0:
                pos, neg = 1 + neg if neg else 0, 1 + pos
            else:
                pos = neg = 0
            ans = max(ans, pos)
        return ans


# Helper function to generate random arrays
def generate_random_array(length, min_val=-10 ** 9, max_val=10 ** 9):
    return [random.randint(min_val, max_val) for _ in range(length)]


# Generate test cases
def generate_test_cases(num_cases=10):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        length = random.randint(1, 10 ** 5)
        nums = generate_random_array(length)

        # Compute expected output using the provided solution
        expected_output = solution.getMaxLen(nums)

        test_cases.append({
            "input": {"nums": nums},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1567.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
