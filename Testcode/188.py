import json
import random
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # solve special cases
        if not prices or k == 0:
            return 0

        # find all consecutively increasing subsequence
        transactions = []
        start = 0
        end = 0
        for i in range(1, n):
            if prices[i] >= prices[i - 1]:
                end = i
            else:
                if end > start:
                    transactions.append([start, end])
                start = i
        if end > start:
            transactions.append([start, end])

        while len(transactions) > k:
            # check delete loss
            delete_index = 0
            min_delete_loss = float("inf")
            for i in range(len(transactions)):
                t = transactions[i]
                profit_loss = prices[t[1]] - prices[t[0]]
                if profit_loss < min_delete_loss:
                    min_delete_loss = profit_loss
                    delete_index = i

            # check merge loss
            merge_index = 0
            min_merge_loss = float("inf")
            for i in range(1, len(transactions)):
                t1 = transactions[i - 1]
                t2 = transactions[i]
                profit_loss = prices[t1[1]] - prices[t2[0]]
                if profit_loss < min_merge_loss:
                    min_merge_loss = profit_loss
                    merge_index = i

            # delete or merge
            if min_delete_loss <= min_merge_loss:
                transactions.pop(delete_index)
            else:
                transactions[merge_index - 1][1] = transactions[merge_index][1]
                transactions.pop(merge_index)

        return sum(prices[j] - prices[i] for i, j in transactions)

def generate_random_prices(length: int, value_range=(0, 1000)) -> List[int]:
    """
    Generates a random list of prices.

    :param length: Number of days (length of the prices list).
    :param value_range: Range of prices for each day.
    :return: List of random prices.
    """
    return [random.randint(value_range[0], value_range[1]) for _ in range(length)]

def generate_test_cases(num_cases=100, max_k=100, max_length=1000, value_range=(0, 1000)):
    """
    Generates test cases for the maxProfit function.

    :param num_cases: Number of test cases to generate.
    :param max_k: Maximum value of k (number of transactions).
    :param max_length: Maximum length of the prices list.
    :param value_range: Range of prices for each day.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize k and the length of the prices list
        k = random.randint(1, max_k)
        length = random.randint(1, max_length)
        prices = generate_random_prices(length, value_range)

        # Calculate the expected output using the provided solution
        expected_output = solution.maxProfit(k, prices)

        # Add test case
        test_cases.append({
            "input": {"k": k, "prices": prices},
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_188.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_k=10, max_length=100, value_range=(0, 1000))

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
