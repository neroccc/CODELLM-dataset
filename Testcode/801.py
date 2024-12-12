import json
import random
from typing import List


class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)

        # Min swaps to get ascending order if we swap at i
        swap = [0] * n
        # Min swaps to get ascending order if we do not swap at i
        noswap = [0] * n

        # Base case: swapping 0th element
        swap[0] = 1

        for i in range(1, n):
            strictly_increasing = A[i] > A[i - 1] and B[i] > B[i - 1]
            strictly_xincreasing = A[i] > B[i - 1] and B[i] > A[i - 1]

            if strictly_increasing and strictly_xincreasing:
                swap[i] = min(noswap[i - 1], swap[i - 1]) + 1
                noswap[i] = min(noswap[i - 1], swap[i - 1])
            elif strictly_increasing:
                swap[i] = swap[i - 1] + 1
                noswap[i] = noswap[i - 1]
            elif strictly_xincreasing:
                swap[i] = noswap[i - 1] + 1
                noswap[i] = swap[i - 1]

        return min(noswap[n - 1], swap[n - 1])


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random length for nums1 and nums2 between 2 and 10^5
        length = random.randint(2, 100)
        # Generate random elements for nums1 and nums2 in the range [0, 2 * 10^5]
        nums1 = [random.randint(0, 200000) for _ in range(length)]
        nums2 = [random.randint(0, 200000) for _ in range(length)]
        # Ensure the input is valid
        nums1.sort()
        nums2.sort()
        # Compute the output using the solution's method
        output = solution.minSwap(nums1, nums2)
        # Append the test case
        test_cases.append({
            "input": {
                "nums1": nums1,
                "nums2": nums2
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_801.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
