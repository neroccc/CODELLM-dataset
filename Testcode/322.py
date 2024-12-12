import json
import random
from typing import List
from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            min_cost = float('inf')
            for coin in coins:
                res = dfs(rem - coin)
                if res != -1:
                    min_cost = min(min_cost, res + 1)
            return min_cost if min_cost != float('inf') else -1

        return dfs(amount)

def generate_random_coins(length: int, value_range=(1, 100)) -> List[int]:
    """
    Generates a random list of coin denominations.

    :param length: Number of coin denominations.
    :param value_range: Range of values for each coin denomination.
    :return: Random list of coin denominations.
    """
    return random.sample(range(value_range[0], value_range[1] + 1), length)

def generate_test_cases(num_cases=100, max_coins=12, max_amount=10**4, coin_value_range=(1, 100)):
    """
    Generates test cases for the coinChange function.

    :param num_cases: Number of test cases to generate.
    :param max_coins: Maximum number of coin denominations.
    :param max_amount: Maximum value for the amount.
    :param coin_value_range: Range of values for coin denominations.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize the number of coin denominations and the amount
        num_coins = random.randint(1, max_coins)
        coins = generate_random_coins(num_coins, coin_value_range)
        amount = random.randint(0, max_amount)

        # Calculate the expected output using the provided solution
        expected_output = solution.coinChange(coins, amount)

        # Add test case
        test_cases.append({
            "input": {"coins": coins, "amount": amount},
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_322.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_coins=10, max_amount=1000, coin_value_range=(1, 50))

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
