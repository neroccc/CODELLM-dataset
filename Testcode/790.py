import json
import random
from typing import List
from functools import cache


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1_000_000_007

        # handle base case scenarios
        if n <= 2:
            return n

        # f[k]: number of ways to "fully cover a board" of width k
        f = [0] * (n + 1)

        # p[k]: number of ways to "partially cover a board" of width k
        p = [0] * (n + 1)

        # initialize f and p with results for the base case scenarios
        f[1] = 1
        f[2] = 2
        p[2] = 1

        for k in range(3, n + 1):
            f[k] = (f[k - 1] + f[k - 2] + 2 * p[k - 1]) % MOD
            p[k] = (p[k - 1] + f[k - 2]) % MOD
        return f[n]


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random value of n between 1 and 1000
        n = random.randint(1, 1000)
        # Compute the output using the solution's method
        output = solution.numTilings(n)
        # Append the test case
        test_cases.append({
            "input": {
                "n": n
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_790.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=1000)
