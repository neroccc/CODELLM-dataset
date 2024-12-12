import json
import random
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost, t2_cost = float("inf"), float("inf")
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            # reinvest the gained profit in the second transaction
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit

def generate_test_cases(num_cases=1000, max_length=10**5, max_price=10**5):
    """
    Generates test cases for the maxProfit function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the prices array.
    :param max_price: Maximum price value.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize the length of the prices array
        length = random.randint(1, min(1000, max_length))  # Adjusted for practical test sizes
        prices = [random.randint(0, max_price) for _ in range(length)]

        # Calculate the expected output using the provided solution
        expected_output = solution.maxProfit(prices)

        # Add test case
        test_cases.append({
            "input": prices,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_123.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=1000, max_length=1000, max_price=100000)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
