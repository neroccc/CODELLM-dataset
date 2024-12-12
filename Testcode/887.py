import json
import random
from math import comb
from bisect import bisect_left

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        return bisect_left(range(0, n), n, key=lambda drops: sum(comb(drops, x) for x in range(1, k + 1)))


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate random values for k and n
        k = random.randint(1, 100)  # Number of eggs
        n = random.randint(1, 10000)  # Number of floors

        # Compute the output using the solution's method
        output = solution.superEggDrop(k, n)

        # Append the test case
        test_cases.append({
            "input": {
                "k": k,
                "n": n
            },
            "output": output
        })

    # Save to a JSON file
    with open("test_cases_887.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
