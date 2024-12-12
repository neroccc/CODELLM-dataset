import json
import random
from typing import List
from functools import lru_cache

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()

        @lru_cache(None)
        def dp(left, right, k):
            if k == 1:
                mid = houses[(left + right) // 2]
                return sum(abs(houses[i] - mid) for i in range(left, right + 1))

            return min(dp(left, i, 1) + dp(i + 1, right, k - 1)
                       for i in range(left, right - k + 2))

        return dp(0, len(houses) - 1, k)

# Helper function to generate random test cases
def generate_houses_and_k():
    num_houses = random.randint(1, 100)
    houses = sorted(random.sample(range(1, 10**4 + 1), num_houses))
    k = random.randint(1, num_houses)
    return houses, k

# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        houses, k = generate_houses_and_k()
        # Compute expected output using the provided solution
        expected_output = solution.minDistance(houses, k)

        test_cases.append({
            "input": {"houses": houses, "k": k},
            "output": expected_output
        })

    # Save to JSON file
    with open("test_cases_1478.json", "w") as f:
        json.dump(test_cases, f, indent=4)

# Generate and save the test cases
generate_test_cases()
