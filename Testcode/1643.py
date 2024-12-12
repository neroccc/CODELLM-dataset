import json
from math import comb
import random


class Solution:
    def kthSmallestPath(self, destination, k):
        v, h = destination
        res = ''
        while h > 0 and v > 0:
            pre = comb(h + v - 1, v)

            if k <= pre:
                res += 'H'
                h -= 1
            else:
                res += 'V'
                v -= 1
                k -= pre

        if h == 0:
            res += 'V' * v
        if v == 0:
            res += 'H' * h

        return res


# Helper function to generate random test cases
def generate_random_test_case():
    row = random.randint(1, 15)
    column = random.randint(1, 15)
    total_paths = comb(row + column, row)
    k = random.randint(1, total_paths)
    return [row, column], k


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        destination, k = generate_random_test_case()
        expected_output = solution.kthSmallestPath(destination, k)

        test_cases.append({
            "input": {"destination": destination, "k": k},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1643.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
