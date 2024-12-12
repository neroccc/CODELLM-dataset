import json
import random
from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7

        length = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(length + 1)]
        dp[0][0][0] = 1
        for i in range(1, length + 1):
            members, earn = group[i - 1], profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    if j < members:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - members][max(0, k - earn)]) % MOD

        total = sum(dp[length][j][minProfit] for j in range(n + 1))
        return total % MOD


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate random values for n and minProfit
        n = random.randint(1, 100)
        minProfit = random.randint(0, 100)
        # Generate random length for group and profit
        length = random.randint(1, 20)  # Keep manageable sizes
        group = [random.randint(1, 100) for _ in range(length)]
        profit = [random.randint(0, 100) for _ in range(length)]

        # Compute the output using the solution's method
        output = solution.profitableSchemes(n, minProfit, group, profit)
        # Append the test case
        test_cases.append({
            "input": {
                "n": n,
                "minProfit": minProfit,
                "group": group,
                "profit": profit
            },
            "output": output
        })

    # Save to a JSON file
    with open("test_cases_879.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
