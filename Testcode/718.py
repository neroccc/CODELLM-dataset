import json
import random
from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        N, M = len(nums1), len(nums2)

        def ok(k):
            # Use binary search to find the length `k`
            s = set(tuple(nums1[i: i + k]) for i in range(N - k + 1))
            return any(tuple(nums2[i: i + k]) in s for i in range(M - k + 1))

        # Initialize possible boundary
        l, r = 0, min(N, M)
        while l < r:
            # Get the middle one (upper half for even elements)
            m = (l + r + 1) // 2
            if ok(m):
                l = m
            else:
                r = m - 1
        return l


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate random lengths for nums1 and nums2 between 1 and 1000
        length1 = random.randint(1, 1000)
        length2 = random.randint(1, 1000)
        # Generate random arrays with elements in range [0, 100]
        nums1 = [random.randint(0, 100) for _ in range(length1)]
        nums2 = [random.randint(0, 100) for _ in range(length2)]
        # Compute the output using the solution's method
        output = solution.findLength(nums1, nums2)
        # Append the test case
        test_cases.append({
            "input": {
                "nums1": nums1,
                "nums2": nums2
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_718.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=1000)
