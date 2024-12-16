import json
import random


# Provided solution to compute expected outputs
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 1000000007
        dp = [0] * (k + 1)
        dp[0] = 1
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                dp[j] = (dp[j] + dp[j - 1]) % MOD
            for j in range(k, i - 1, -1):
                dp[j] = (dp[j] - dp[j - i] + MOD) % MOD
        return dp[k]


def generate_test_cases(num_cases=1000):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Generate random values for n and k within the constraints
        n = random.randint(1, 1000)
        k = random.randint(0, 1000)

        # Compute the expected output using the provided solution
        expected_output = solution.kInversePairs(n, k)

        # Append the test case
        test_cases.append({
            "input": {"n": n, "k": k},
            "output": expected_output
        })

    return test_cases


# Generate and save test cases
def save_test_cases_to_file(filename="test_cases_629.json", num_cases=100):
    test_cases = generate_test_cases(num_cases)
    with open(filename, "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate 1000 test cases and save them
save_test_cases_to_file()
