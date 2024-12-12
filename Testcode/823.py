import json
import random
from typing import List
import math


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        total_nums = len(arr)
        moduler = 1000000007
        count_product_dict = {num: 1 for num in arr}
        arr.sort()

        for i in range(1, total_nums):
            for j in range(i):
                quotient = arr[i] // arr[j]
                if quotient < 2 or math.sqrt(arr[i]) > arr[i - 1]:
                    break
                if arr[i] % arr[j] == 0:
                    count_product_dict[arr[i]] += count_product_dict[arr[j]] * count_product_dict.get(quotient, 0)
                    count_product_dict[arr[i]] %= moduler

        return sum(count_product_dict.values()) % moduler


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random length for arr between 1 and 1000
        length = random.randint(1, 100)
        # Generate random elements for arr in the range [2, 10^9]
        arr = sorted(random.sample(range(2, 10 ** 4), length))  # Reduce upper range for practical computation
        # Compute the output using the solution's method
        output = solution.numFactoredBinaryTrees(arr)
        # Append the test case
        test_cases.append({
            "input": {
                "arr": arr
            },
            "output": output
        })

    # Save to a JSON file
    with open("test_cases_823.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
