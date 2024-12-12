import json
import random
from typing import List
from functools import lru_cache


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        ppl = dict()  # mapping: hat -> people
        for i, hat in enumerate(hats):
            for x in hat:
                ppl.setdefault(x, []).append(i)

        @lru_cache(None)
        def fn(h, mask):
            """Return the number of ways to assign h hats among people in mask."""
            if mask == (1 << len(hats)) - 1:
                return 1  # All people have hats
            if h == 40:
                return 0  # Out of hats
            ans = fn(h + 1, mask)
            for p in ppl.get(h + 1, []):
                if mask & (1 << p):
                    continue  # Already has a hat
                mask |= 1 << p  # Assign hat
                ans += fn(h + 1, mask)
                mask ^= 1 << p  # Reset assignment
            return ans % 1_000_000_007

        return fn(0, 0)


# Generate test cases
def generate_test_cases(num_cases=100):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Randomly generate the number of people
        n = random.randint(1, 10)
        # Generate hat preferences for each person
        hats = [random.sample(range(1, 41), random.randint(1, 40)) for _ in range(n)]
        # Compute the expected output using the solution
        expected_output = solution.numberWays(hats)
        # Add the test case to the list
        test_cases.append({"hats": hats, "output": expected_output})

    # Save the test cases to a file
    with open("test_cases_1434.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate 10 test cases
generate_test_cases()
