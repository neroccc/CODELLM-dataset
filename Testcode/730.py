import json
import random
from typing import List
from functools import lru_cache

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:

        @lru_cache(None)
        def dp(left: int, rght: int, res=0):
            for ch in 'abcd':
                l, r = s.find(ch, left, rght), s.rfind(ch, left, rght)
                res += 0 if l == -1 else 1 if l == r else dp(l + 1, r) + 2
            return res % 1_000_000_007

        return dp(0, len(s))


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random string of length between 1 and 1000 consisting of 'a', 'b', 'c', 'd'
        length = random.randint(1, 1000)
        s = ''.join(random.choices('abcd', k=length))
        # Compute the output using the solution's method
        output = solution.countPalindromicSubsequences(s)
        # Append the test case
        test_cases.append({
            "input": {
                "s": s
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_730.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
