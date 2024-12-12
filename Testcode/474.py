import json
import random
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        counter = [[s.count("0"), s.count("1")] for s in strs]

        for zeroes, ones in counter:
            for i in range(m, zeroes - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeroes][j - ones])

        return dp[-1][-1]


def generate_test_cases(solution, num_cases=100):
    test_cases = []

    for _ in range(num_cases):
        # Generate a random number of strings
        num_strs = random.randint(1, 20)  # Small range for efficiency
        strs = []

        # Create random binary strings
        for _ in range(num_strs):
            length = random.randint(1, 10)  # Length of each binary string
            binary_string = ''.join(random.choices('01', k=length))
            strs.append(binary_string)

        # Generate random values for m and n
        m = random.randint(1, 20)
        n = random.randint(1, 20)

        # Calculate expected output
        expected_output = solution.findMaxForm(strs, m, n)

        # Add test case
        test_cases.append({
            "input": {"strs": strs, "m": m, "n": n},
            "output": expected_output
        })

    return test_cases


# Instantiate the solution and generate test cases
solution = Solution()
test_cases = generate_test_cases(solution, num_cases=1000)

# Save the test cases to a JSON file
file_path = "../test_cases_474.json"
with open(file_path, "w") as file:
    json.dump(test_cases, file, indent=2)

print(f"Test cases have been saved to {file_path}.")
