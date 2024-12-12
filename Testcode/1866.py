import json
import random
from functools import lru_cache


class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        @lru_cache(None)
        def fn(n, k):
            """Return number of ways to rearrange n sticks so that k are visible."""
            if n == k:
                return 1
            if k == 0:
                return 0
            return ((n - 1) * fn(n - 1, k) + fn(n - 1, k - 1)) % 1_000_000_007

        return fn(n, k)


# Generate random test cases
def generate_test_cases(num_cases=50, max_n=1000):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(1, max_n)
        k = random.randint(1, n)
        expected_output = solution.rearrangeSticks(n, k)

        test_cases.append({
            "input": {"n": n, "k": k},
            "output": expected_output
        })

    # Save to a file
    with open("test_cases_1866.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
