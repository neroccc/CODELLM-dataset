import json
import random
from typing import List

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j, group):
            if i == len(cost) and group == target: return 0
            if i >= len(cost): return float("inf")
            if group > target: return float("inf")

            res = float("inf")
            if not houses[i]:
                for color in range(1, n + 1):
                    if j != color:
                        res = min(res, dp(i + 1, color, group + 1) + cost[i][color - 1])
                    else:
                        res = min(res, dp(i + 1, color, group) + cost[i][color - 1])
            else:
                color = houses[i]
                res = dp(i + 1, color, group + 1) if j != color else dp(i + 1, color, group)

            return res

        res = dp(0, -1, 0)
        return -1 if res == float("inf") else res

# Helper function to generate random houses and cost
def generate_input(m, n):
    houses = [random.randint(0, n) for _ in range(m)]
    cost = [[random.randint(1, 10**4) for _ in range(n)] for _ in range(m)]
    target = random.randint(1, m)
    return houses, cost, target

# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        m = random.randint(1, 100)  # Number of houses
        n = random.randint(1, 20)  # Number of colors
        houses, cost, target = generate_input(m, n)

        # Compute the expected output using the provided solution
        expected_output = solution.minCost(houses, cost, m, n, target)

        test_cases.append({
            "input": {"houses": houses, "cost": cost, "m": m, "n": n, "target": target},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1473.json", "w") as f:
        json.dump(test_cases, f, indent=4)

# Generate and save the test cases
generate_test_cases()
