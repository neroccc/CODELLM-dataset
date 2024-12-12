import json
import random
from functools import lru_cache


class Solution:
    def minimumXORSum(self, a, b):
        @lru_cache(None)
        def dp(mask: int) -> int:
            i = bin(mask).count("1")
            if i >= len(a):
                return 0
            return min((a[i] ^ b[j]) + dp(mask + (1 << j))
                       for j in range(len(b)) if mask & (1 << j) == 0)

        return dp(0)


# Function to generate random test cases
def generate_test_cases(num_cases=50, max_n=14, max_value=10 ** 7):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomly determine the size of the arrays
        n = random.randint(1, max_n)

        # Generate two random arrays of size n
        nums1 = [random.randint(0, max_value) for _ in range(n)]
        nums2 = [random.randint(0, max_value) for _ in range(n)]

        # Calculate the expected output using the provided solution
        expected_output = solution.minimumXORSum(nums1, nums2)

        test_cases.append({
            "input": {"nums1": nums1, "nums2": nums2},
            "output": expected_output
        })

    # Save the test cases to a JSON file
    with open("test_cases_1879.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save test cases
generate_test_cases()
