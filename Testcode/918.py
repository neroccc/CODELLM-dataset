import json
import random
import math
from typing import List

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        totalSum = 0
        currMaxSum = 0
        currMinSum = 0
        maxSum = -math.inf
        minSum = math.inf

        for a in A:
            totalSum += a
            currMaxSum = max(currMaxSum + a, a)
            currMinSum = min(currMinSum + a, a)
            maxSum = max(maxSum, currMaxSum)
            minSum = min(minSum, currMinSum)

        return maxSum if maxSum < 0 else max(maxSum, totalSum - minSum)


def generate_test_cases(num_cases=10):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Generate a random array length between 1 and 10,000
        n = random.randint(1, 1000)  # Adjust size for faster computation if needed
        # Generate a random array with values between -30,000 and 30,000
        nums = [random.randint(-30000, 30000) for _ in range(n)]

        # Compute the expected output using the solution
        output = solution.maxSubarraySumCircular(nums)

        # Append the test case
        test_cases.append({
            "input": {"nums": nums},
            "output": output
        })

    # Save to a JSON file
    with open("test_cases_918.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=10)
