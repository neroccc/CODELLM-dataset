import json
import random
from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, free = -prices[0], 0

        for i in range(1, n):
            tmp = hold
            hold = max(hold, free - prices[i])
            free = max(free, tmp + prices[i] - fee)

        return free


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random length for prices between 1 and 50,000
        length = random.randint(1, 50000)
        # Generate random prices in the range [1, 50,000)
        prices = [random.randint(1, 49999) for _ in range(length)]
        # Generate a random fee in the range [0, 50,000)
        fee = random.randint(0, 49999)
        # Compute the output using the solution's method
        output = solution.maxProfit(prices, fee)
        # Append the test case
        test_cases.append({
            "input": {
                "prices": prices,
                "fee": fee
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_714.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
