import json
import random
from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = {0}
        for st in stones:
            tmp = set()
            for i in s:
                tmp.add(abs(i + st))
                tmp.add(abs(i - st))
            s = tmp
        return min(s) if len(s) > 0 else 0


def generate_random_stones(min_length=1, max_length=30, max_value=100):
    """Generate a random list of stone weights."""
    length = random.randint(min_length, max_length)
    return [random.randint(1, max_value) for _ in range(length)]


def generate_test_cases(num_cases=50, max_length=30, max_value=100):
    """Generate test cases for the Last Stone Weight II problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        stones = generate_random_stones(1, max_length, max_value)
        expected_output = solution.lastStoneWeightII(stones)
        test_cases.append({
            "input": stones,
            "output": expected_output
        })

    # Add predefined edge cases
    predefined_cases = [
        {"input": [2, 7, 4, 1, 8, 1], "output": solution.lastStoneWeightII([2, 7, 4, 1, 8, 1])},
        {"input": [31, 26, 33, 21, 40], "output": solution.lastStoneWeightII([31, 26, 33, 21, 40])},
        {"input": [1, 1], "output": solution.lastStoneWeightII([1, 1])},
        {"input": [10], "output": solution.lastStoneWeightII([10])},
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
    max_length = 30
    max_value = 100
    test_cases = generate_test_cases(num_cases, max_length, max_value)
    save_test_cases("../test_cases_1049.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'last_stone_weight_test_cases.json'.")
