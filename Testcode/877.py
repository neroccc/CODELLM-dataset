import json
import random
from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Allocate the space for DP
        dp = [[0] * len(piles) for _ in range(len(piles))]

        # Initial conditions: when there is only one pile
        for i in range(len(piles)):
            dp[i][i] = piles[i]

        # Fill DP table for all gaps (from small to large gaps)
        for d in range(1, len(piles)):
            for i in range(len(piles) - d):
                dp[i][i + d] = max(
                    piles[i] - dp[i + 1][i + d],
                    piles[i + d] - dp[i][i + d - 1]
                )

        return dp[0][-1] > 0


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random even length for the array
        length = random.randint(2, 500) // 2 * 2
        # Generate an array of random positive integers
        piles = [random.randint(1, 500) for _ in range(length)]
        # Ensure the sum of the array is odd
        if sum(piles) % 2 == 0:
            piles[0] += 1

        # Compute the output using the solution's method
        output = solution.stoneGame(piles)
        # Append the test case
        test_cases.append({
            "input": {
                "piles": piles
            },
            "output": output
        })

    # Save to a JSON file
    with open("test_cases_877.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
