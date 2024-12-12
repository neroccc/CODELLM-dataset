import json
import random


class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        mod = 10 ** 9 + 7
        dp = [[0, 0] for _ in range(2)]
        n = len(binary)

        for ch in binary:
            if ch == '0':
                dp[0][0] = 1
                dp[1][0] = (dp[1][0] + dp[1][1]) % mod
            else:
                dp[1][1] = (dp[1][0] + dp[1][1] + 1) % mod

        return (dp[0][0] + dp[0][1] + dp[1][0] + dp[1][1]) % mod


def generate_test_cases(num_cases=100, max_length=10 ** 5):
    """Generate random test cases for the problem."""
    test_cases = []
    for _ in range(num_cases):
        length = random.randint(1, min(100, max_length))  # Limit length for practicality
        binary = ''.join(random.choice('01') for _ in range(length))
        test_cases.append(binary)
    return test_cases


def compute_expected_outputs(test_cases):
    """Compute the expected outputs for the test cases."""
    solution = Solution()
    outputs = []
    for binary in test_cases:
        output = solution.numberOfUniqueGoodSubsequences(binary)
        outputs.append(output)
    return outputs


# Generate test cases
test_cases = generate_test_cases(num_cases=50, max_length=100)

# Compute expected outputs
expected_outputs = compute_expected_outputs(test_cases)

# Save test cases and outputs to a JSON file
test_data = [{"input": binary, "output": output} for binary, output in zip(test_cases, expected_outputs)]

with open("test_cases_1987.json", "w") as f:
    json.dump(test_data, f, indent=4)

print("Test cases generated and saved to 'test_case_.json'")
