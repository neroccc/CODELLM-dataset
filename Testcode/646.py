import json
import random

class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        ans, chainEnd = 0, float('-inf')
        pairs.sort(key=lambda x: x[1])

        for l, r in pairs:
            if l > chainEnd:
                ans += 1
                chainEnd = r

        return ans


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random number of pairs (1 to 1000)
        n = random.randint(1, 1000)
        # Generate random pairs such that left < right
        pairs = [[random.randint(-1000, 999), random.randint(-999, 1000)] for _ in range(n)]
        pairs = [[l, r] for l, r in pairs if l < r]
        # Compute the output using the solution's method
        output = solution.findLongestChain(pairs)
        # Append the test case
        test_cases.append({
            "input": {
                "pairs": pairs
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_646.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=1000)
