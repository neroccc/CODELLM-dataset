import json
import random
from functools import lru_cache
from math import sqrt, floor

class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        if not n:
            return False
        for i in reversed(range(1, floor(sqrt(n)) + 1)):
            if not self.winnerSquareGame(n - i**2):
                return True
        return False

# Generate test cases
def generate_test_cases(num_cases=1000):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(1, 10**5)
        # Compute expected output using the provided solution
        expected_output = solution.winnerSquareGame(n)

        test_cases.append({
            "input": {"n": n},
            "output": expected_output
        })

    # Save test cases to a JSON file
    with open("test_cases_1510.json", "w") as f:
        json.dump(test_cases, f, indent=4)

# Generate and save the test cases
generate_test_cases()
