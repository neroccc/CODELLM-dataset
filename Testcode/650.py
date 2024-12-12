import json
import random


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        steps = 0
        factor = 2

        while n > 1:
            while n % factor == 0:
                steps += factor
                n //= factor
            factor += 1

        return steps


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random value for n between 1 and 1000
        n = random.randint(1, 1000)
        # Compute the output using the solution's method
        output = solution.minSteps(n)
        # Append the test case
        test_cases.append({
            "input": {
                "n": n
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_650.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=1000)
