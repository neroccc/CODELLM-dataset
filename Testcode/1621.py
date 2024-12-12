import json
import random
from functools import lru_cache


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        M = 10 ** 9 + 7

        @lru_cache(None)
        def helper(idx, rem, isInMiddle):
            if idx == n - 1:
                return 0 if rem else 1
            ans = 0
            if isInMiddle:
                ans += helper(idx + 1, rem, isInMiddle)
                ans %= M
                ans += helper(idx + 1, rem, not isInMiddle)
                ans %= M
                if rem > 0:
                    ans += helper(idx + 1, rem - 1, isInMiddle)
                    ans %= M
            else:
                ans += helper(idx + 1, rem, isInMiddle)
                ans %= M
                if rem > 0:
                    ans += helper(idx + 1, rem - 1, not isInMiddle)
                    ans %= M
            return ans

        return helper(0, k, False)


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(2, 1000)
        k = random.randint(1, n - 1)
        expected_output = solution.numberOfSets(n, k)

        test_cases.append({
            "input": {"n": n, "k": k},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1621.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
