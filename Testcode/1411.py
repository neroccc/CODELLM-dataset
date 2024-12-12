import json
import random


class Solution:
    def numOfWays(self, n: int, x=0, y=3, mod=1_000_000_007) -> int:
        for _ in range(n):
            x, y = (3 * x + 2 * y) % mod, (2 * x + 2 * y) % mod
        return (x + y) % mod


# Generate test cases
def generate_test_cases(num_cases=100):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Randomly generate the number of rows (n)
        n = random.randint(1, 5000)
        # Compute the expected output using the solution
        expected_output = solution.numOfWays(n)
        # Add the test case to the list
        test_cases.append({"n": n, "output": expected_output})

    # Save the test cases to a file
    with open("test_cases_1411.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate 10 test cases
generate_test_cases()
