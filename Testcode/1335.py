import json
import random
from typing import List
from functools import lru_cache
from math import inf


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @lru_cache(None)
        def dp(idx, d, curr):
            if idx == len(jobDifficulty) and d == 0:
                return curr
            if idx >= len(jobDifficulty) or d <= 0:
                return inf
            return min(dp(idx + 1, d, max(curr, jobDifficulty[idx])),
                       max(curr, jobDifficulty[idx]) + dp(idx + 1, d - 1, 0))

        ans = dp(0, d, 0)
        return ans if ans != inf else -1


# Generate test cases
def generate_test_cases(num_cases=100):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Randomly decide the length of jobDifficulty
        length = random.randint(1, 300)
        # Generate a random jobDifficulty array
        jobDifficulty = [random.randint(0, 1000) for _ in range(length)]
        # Randomly choose a valid number of days
        d = random.randint(1, min(len(jobDifficulty), 10))
        # Compute the expected output
        expected_output = solution.minDifficulty(jobDifficulty, d)
        # Add the test case to the list
        test_cases.append({"jobDifficulty": jobDifficulty, "d": d, "output": expected_output})

    # Save the test cases to a file
    with open("test_cases_1335.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate 1000 test cases
generate_test_cases()
