import json
import random
from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        W = []  # Array of sums of windows
        curr_sum = 0
        for i, x in enumerate(nums):
            curr_sum += x
            if i >= k:
                curr_sum -= nums[i - k]
            if i >= k - 1:
                W.append(curr_sum)

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for j in range(k, len(W) - k):
            i, l = left[j - k], right[j + k]
            if ans is None or (W[i] + W[j] + W[l] > W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, l
        return list(ans)


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random array of length between 3 * k and 20000
        n = random.randint(3, 20000)
        nums = [random.randint(1, 2**16 - 1) for _ in range(n)]
        # Generate a random value for k within valid range
        k = random.randint(1, n // 3)
        # Compute the output using the solution's method
        output = solution.maxSumOfThreeSubarrays(nums, k)
        # Append the test case
        test_cases.append({
            "input": {
                "nums": nums,
                "k": k
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_689.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
