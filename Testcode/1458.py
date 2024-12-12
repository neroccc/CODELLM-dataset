import json
import random
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                curr_product = nums1[i - 1] * nums2[j - 1]

                dp[i][j] = max(dp[i][j], curr_product, dp[i - 1][j], dp[i][j - 1], curr_product + dp[i - 1][j - 1])

        return dp[m][n]


# Helper function to generate random arrays
def generate_arrays():
    length1 = random.randint(1, 500)
    length2 = random.randint(1, 500)
    nums1 = [random.randint(-1000, 1000) for _ in range(length1)]
    nums2 = [random.randint(-1000, 1000) for _ in range(length2)]
    return nums1, nums2


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        nums1, nums2 = generate_arrays()

        # Compute the expected output using the provided solution
        expected_output = solution.maxDotProduct(nums1, nums2)

        test_cases.append({
            "input": {"nums1": nums1, "nums2": nums2},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1458.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
