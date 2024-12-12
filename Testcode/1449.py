import json
import random
from typing import List
from functools import lru_cache


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:

        @lru_cache(None)
        def fn(x):
            """Return max integer given target x."""
            if x == 0: return 0
            if x < 0: return float('-inf')
            return max(fn(x - c) * 10 + i + 1 for i, c in enumerate(cost))

        return str(max(0, fn(target)))


# Helper function to generate random costs and targets
def generate_costs_and_target():
    costs = [random.randint(1, 5000) for _ in range(9)]
    target = random.randint(1, 5000)
    return costs, target


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        cost, target = generate_costs_and_target()

        # Compute the expected output using the provided solution
        expected_output = solution.largestNumber(cost, target)

        test_cases.append({
            "input": {"cost": cost, "target": target},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1449.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
