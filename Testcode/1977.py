import json
import random
from typing import List


class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)
        lcs = [[0] * (n + 1) for _ in range(n)]
        for i in reversed(range(n)):
            for j in reversed(range(i + 1, n)):
                if num[i] == num[j]:
                    lcs[i][j] = 1 + lcs[i + 1][j + 1]

        def cmp(i, j, d):
            """Return True if """
            m = lcs[i][j]
            if m >= d:
                return True
            return num[i + m] <= num[j + m]

        dp = [[0] * (n + 1) for _ in range(n)]
        for i in range(n):
            if num[i] != "0":
                for j in range(i + 1, n + 1):
                    if i == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i][j - 1]
                        if 2 * i - j >= 0 and cmp(2 * i - j, i, j - i):
                            dp[i][j] += dp[2 * i - j][i]
                        if 2 * i - j + 1 >= 0 and not cmp(2 * i - j + 1, i, j - i - 1):
                            dp[i][j] += dp[2 * i - j + 1][i]
        return sum(dp[i][n] for i in range(n)) % 1_000_000_007


def generate_test_cases(num_cases=100, max_length=3500):
    """Generate random test cases for the problem."""
    test_cases = []
    for _ in range(num_cases):
        length = random.randint(1, min(100, max_length))  # Limit length for practicality
        num = ''.join(random.choice('0123456789') for _ in range(length))
        test_cases.append(num)
    return test_cases


def compute_expected_outputs(test_cases):
    """Compute the expected outputs for the test cases."""
    solution = Solution()
    outputs = []
    for num in test_cases:
        output = solution.numberOfCombinations(num)
        outputs.append(output)
    return outputs


# Generate test cases
test_cases = generate_test_cases(num_cases=50, max_length=100)

# Compute expected outputs
expected_outputs = compute_expected_outputs(test_cases)

# Save test cases and outputs to a JSON file
test_data = [{"input": num, "output": output} for num, output in zip(test_cases, expected_outputs)]

with open("test_cases_1977.json", "w") as f:
    json.dump(test_data, f, indent=4)

print("Test cases generated and saved to 'test_case_.json'")
