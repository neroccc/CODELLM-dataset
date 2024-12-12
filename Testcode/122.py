import json
import random
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        valley = prices[0]
        peak = prices[0]
        maxprofit = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            maxprofit += peak - valley
        return maxprofit

def generate_test_cases(num_cases=1000, max_length=30000, max_price=10000):
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
        length = random.randint(1, min(100, max_length))  # Keeping length manageable for testing
        prices = [random.randint(0, max_price) for _ in range(length)]

        # Calculate the expected output using the provided solution
        expected_output = solution.maxProfit(prices)

        # Add test case
        test_cases.append({
            "input": prices,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_122.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=1000, max_length=100, max_price=10000)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
