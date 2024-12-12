import json
import random
from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        operations = 0
        monostack = [(0, 0)]  # (height, work to make it)
        for h in target:
            work = max(0, h - monostack[-1][0])

            # Remove smaller buildings from the stack
            while monostack and h >= monostack[-1][0]:
                _, prev_work = monostack.pop()
                operations += prev_work
            monostack.append((h, work))

        # Add remaining work in the stack
        while monostack:
            operations += monostack.pop()[1]
        return operations


# Helper function to generate random target arrays
def generate_random_target(length, max_value=10 ** 5):
    return [random.randint(1, max_value) for _ in range(length)]


# Generate test cases
def generate_test_cases(num_cases=10):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        length = random.randint(1, 10 ** 5)
        target = generate_random_target(length)

        # Compute expected output using the provided solution
        expected_output = solution.minNumberOperations(target)

        test_cases.append({
            "input": {"target": target},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1526.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
