import json
import random
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]


def generate_test_cases(solution, num_cases=100):
    test_cases = []

    for _ in range(num_cases):
        # Generate random amount and coin denominations
        amount = random.randint(0, 100)  # Amount between 0 and 100 for computational feasibility
        num_coins = random.randint(1, 10)  # Number of coin types
        coins = random.sample(range(1, 50), num_coins)  # Unique coins with values between 1 and 50

        # Calculate expected output using the provided solution
        expected_output = solution.change(amount, coins)

        # Add test case
        test_cases.append({
            "input": {"amount": amount, "coins": coins},
            "output": expected_output
        })

    return test_cases


# Instantiate the solution and generate test cases
solution = Solution()
test_cases = generate_test_cases(solution, num_cases=1000)

# Save the test cases to a JSON file
file_path = "../test_cases_518.json"
with open(file_path, "w") as file:
    json.dump(test_cases, file, indent=2)

print(f"Test cases have been saved to {file_path}.")
