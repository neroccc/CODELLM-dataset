import json
import random
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        freq = [0] * (max(nums) + 1)
        for n in nums:
            freq[n] += n

        dp = [0] * len(freq)
        dp[1] = freq[1]
        for i in range(2, len(freq)):
            dp[i] = max(freq[i] + dp[i - 2], dp[i - 1])

        return dp[len(freq) - 1]


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random array of length between 1 and 20,000
        length = random.randint(1, 20000)
        # Generate random elements in the range [1, 10,000]
        nums = [random.randint(1, 10000) for _ in range(length)]
        # Compute the output using the solution's method
        output = solution.deleteAndEarn(nums)
        # Append the test case
        test_cases.append({
            "input": {
                "nums": nums
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_740.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
