import json
import random
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = len(prices)
        # padding the array with additional zero to simplify the logic
        MP = [0] * (L + 2)

        for i in range(L - 1, -1, -1):
            C1 = 0
            # Case 1). buy and sell the stock
            for sell in range(i + 1, L):
                profit = (prices[sell] - prices[i]) + MP[sell + 2]
                C1 = max(profit, C1)

            # Case 2). do no transaction with the stock prices[i]
            C2 = MP[i + 1]

            # sum up two cases
            MP[i] = max(C1, C2)

        return MP[0]

def generate_random_prices(length: int, value_range=(0, 1000)) -> List[int]:
    """
    Generates a random list of stock prices.

    :param length: Number of days (length of the prices list).
    :param value_range: Range of prices for each day.
    :return: List of random prices.
    """
    return [random.randint(value_range[0], value_range[1]) for _ in range(length)]

def generate_test_cases(num_cases=100, max_length=5000, value_range=(0, 1000)):
    """
    Generates test cases for the maxProfit function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the prices list.
    :param value_range: Range of prices for each day.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize the length of the prices list
        length = random.randint(1, min(max_length, 500))
        prices = generate_random_prices(length, value_range)

        # Calculate the expected output using the provided solution
        expected_output = solution.maxProfit(prices)

        # Add test case
        test_cases.append({
            "input": prices,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_309.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_length=100, value_range=(0, 1000))

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
