import json
import random
from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        sumOfMinimums = 0

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                leftBoundary = stack[-1] if stack else -1
                rightBoundary = i

                count = (mid - leftBoundary) * (rightBoundary - mid) % MOD

                sumOfMinimums += (count * arr[mid]) % MOD
                sumOfMinimums %= MOD
            stack.append(i)

        return int(sumOfMinimums)


def generate_test_cases(num_cases=100):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Generate random values for arr
        arr_length = random.randint(1, 1000)  # Limit length for practical computation
        arr = [random.randint(1, 30000) for _ in range(arr_length)]

        # Compute the output using the solution's method
        output = solution.sumSubarrayMins(arr)
        # Append the test case
        test_cases.append({
            "input": {
                "arr": arr
            },
            "output": output
        })

    # Save to a JSON file
    with open("test_cases_907.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
