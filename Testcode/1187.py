import json
import random
from typing import List
from bisect import bisect_right
from functools import cache
from sys import maxsize

class Solution:
    def makeArrayIncreasing(self, first: List[int], second: List[int]) -> int:
        @cache
        def dp(i: int, prev_max: int) -> int:
            if i == len(first):
                return 0

            j = bisect_right(second, prev_max)

            return min(
                dp(i + 1, first[i]) if first[i] > prev_max else maxsize,
                dp(i + 1, second[j]) + 1 if j < len(second) else maxsize,
            )

        second.sort()
        operations = dp(0, -maxsize)
        return operations if operations != maxsize else -1


def generate_random_array(min_length=1, max_length=200, max_value=10**9):
    """Generate a random array of integers."""
    length = random.randint(min_length, max_length)
    return [random.randint(0, max_value) for _ in range(length)]


def generate_test_cases(num_cases=50, max_length=200):
    """Generate test cases for the Make Array Strictly Increasing problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        arr1 = generate_random_array(1, max_length)
        arr2 = generate_random_array(1, max_length)
        expected_output = solution.makeArrayIncreasing(arr1, arr2)
        test_cases.append({"input": {"arr1": arr1, "arr2": arr2}, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": {"arr1": [1, 5, 3, 6, 7], "arr2": [1, 3, 2, 4]}, "output": solution.makeArrayIncreasing([1, 5, 3, 6, 7], [1, 3, 2, 4])},
        {"input": {"arr1": [1, 5, 3, 6, 7], "arr2": [4, 3, 1]}, "output": solution.makeArrayIncreasing([1, 5, 3, 6, 7], [4, 3, 1])},
        {"input": {"arr1": [1, 5, 3, 6, 7], "arr2": [1, 6, 3, 3]}, "output": solution.makeArrayIncreasing([1, 5, 3, 6, 7], [1, 6, 3, 3])},
        {"input": {"arr1": [1], "arr2": [2]}, "output": solution.makeArrayIncreasing([1], [2])},
        {"input": {"arr1": [10, 20, 30], "arr2": [1, 2, 3]}, "output": solution.makeArrayIncreasing([10, 20, 30], [1, 2, 3])},
    ]
    test_cases.extend(predefined_cases)

    return test_cases


def save_test_cases(filename, test_cases):
    """Save test cases to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(test_cases, f, indent=4)


# Generate and save test cases
if __name__ == "__main__":
    num_cases = 100
    max_length = 200
    test_cases = generate_test_cases(num_cases, max_length)
    save_test_cases("test_cases_1187.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'make_array_increasing_test_cases.json'.")
