import json
import random
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * m for _ in range(m + 1)]

        for i in reversed(range(m)):
            for j in range(i, m):
                k = i + m - j - 1
                dp[i][j] = max(nums[i] * multipliers[k] + dp[i + 1][j], nums[j - m + n] * multipliers[k] + dp[i][j - 1])

        return dp[0][-1]


# Helper function to generate random inputs
def generate_random_inputs(max_n, max_m, value_range=(-1000, 1000)):
    n = random.randint(1, max_n)
    m = random.randint(1, min(300, n))  # Ensure m <= 300 and m <= n
    nums = [random.randint(*value_range) for _ in range(n)]
    multipliers = [random.randint(*value_range) for _ in range(m)]
    return nums, multipliers


# Generate test cases
def generate_test_cases(num_cases=100, max_n=100, max_m=300):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        nums, multipliers = generate_random_inputs(max_n, max_m)
        expected_output = solution.maximumScore(nums, multipliers)

        test_cases.append({
            "input": {"nums": nums, "multipliers": multipliers},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1770.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
