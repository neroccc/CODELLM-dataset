import json
import random
from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        if m < n:
            nums1, nums2, m, n = nums2, nums1, n, m
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                curr = dp[j]
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j - 1], curr)
                prev = curr
        return dp[n]


def generate_random_array(max_length=500, max_value=2000):
    """Generate a random array of integers."""
    length = random.randint(1, max_length)
    return [random.randint(1, max_value) for _ in range(length)]


def generate_test_cases(num_cases=50, max_length=500, max_value=2000):
    """Generate test cases for the Maximum Uncrossed Lines problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        nums1 = generate_random_array(max_length, max_value)
        nums2 = generate_random_array(max_length, max_value)
        expected_output = solution.maxUncrossedLines(nums1, nums2)
        test_cases.append({
            "input": {
                "nums1": nums1,
                "nums2": nums2
            },
            "output": expected_output
        })

    # Add predefined edge cases
    predefined_cases = [
        {"input": {"nums1": [1, 4, 2], "nums2": [1, 2, 4]},
         "output": solution.maxUncrossedLines([1, 4, 2], [1, 2, 4])},
        {"input": {"nums1": [2, 5, 1, 2, 5], "nums2": [10, 5, 2, 1, 5, 2]},
         "output": solution.maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2])},
        {"input": {"nums1": [1, 3, 7, 1, 7, 5], "nums2": [1, 9, 2, 5, 1]},
         "output": solution.maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1])},
    ]
    test_cases.extend(predefined_cases)

    return test_cases


def save_test_cases(filename, test_cases):
    """Save test cases to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(test_cases, f, indent=4)


# Generate and save test cases
if __name__ == "__main__":
    num_cases = 100
    max_length = 500
    max_value = 2000
    test_cases = generate_test_cases(num_cases, max_length, max_value)
    save_test_cases("../test_cases_1035.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'max_uncrossed_lines_test_cases.json'.")
