import json
import random
from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        m, dp, cnt = 0, [1] * n, [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1: dp[i], cnt[i] = dp[j] + 1, cnt[j]
                    elif dp[i] == dp[j] + 1: cnt[i] += cnt[j]
            m = max(m, dp[i])
        return sum(c for l, c in zip(dp, cnt) if l == m)


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random array of length between 1 and 2000
        length = random.randint(1, 2000)
        nums = [random.randint(-10**6, 10**6) for _ in range(length)]
        # Compute the output using the solution's method
        output = solution.findNumberOfLIS(nums)
        # Append the test case
        test_cases.append({
            "input": {
                "nums": nums
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_673.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=1000)
