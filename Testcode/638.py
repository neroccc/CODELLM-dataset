import json
import math
from typing import List
import random


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def _impl(current_needs, dp_table):
            if current_needs in dp_table:
                return dp_table[current_needs]
            length = len(price)
            min_price = float("inf")

            for spec in special:
                can_use = True
                for i in range(length):
                    if spec[i] > current_needs[i]:
                        can_use = False
                        break
                if can_use:
                    current_price = spec[-1] + _impl(
                        tuple([need - consume for consume, need in zip(spec, current_needs)]),
                        dp_table
                    )
                    if current_price < min_price:
                        min_price = current_price

            if not math.isinf(min_price):
                dp_table[current_needs] = min_price
                return min_price

            current_price = 0
            for i, n in enumerate(current_needs):
                current_price += n * price[i]

            dp_table[current_needs] = current_price
            return current_price

        length = len(price)
        useful_special = []
        for spec in special:
            current = 0
            for i in range(length):
                current += price[i] * spec[i]
            if current > spec[-1]:
                useful_special.append(spec)
        special = useful_special
        return _impl(tuple(needs), {})

def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Randomly generate n, the number of items (1 to 6)
        n = random.randint(1, 6)
        # Generate random prices for n items
        price = [random.randint(1, 10) for _ in range(n)]
        # Generate random needs for n items
        needs = [random.randint(0, 10) for _ in range(n)]
        # Generate a random number of special offers
        num_special = random.randint(1, 100)
        special = []
        for _ in range(num_special):
            offer = [random.randint(0, 50) for _ in range(n)]
            offer.append(random.randint(1, 50))  # Add the price of the offer
            special.append(offer)
        # Compute the output using the solution's method
        output = solution.shoppingOffers(price, special, needs)
        # Append the test case
        test_cases.append({
            "input": {
                "price": price,
                "special": special,
                "needs": needs
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_638.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=1000)
