import json
import random
from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n

        # Handle the first k indices differently
        for j in range(k):
            dp[j] = max(arr[:j + 1]) * (j + 1)

        # Calculate the maximum sum using dynamic programming
        for j in range(k, n):
            curr = []
            for m in range(k):
                curr.append(dp[j - m - 1] + max(arr[(j - m):(j + 1)]) * (m + 1))
            dp[j] = max(curr)

        return dp[-1]


def generate_random_array(min_length=1, max_length=500, max_value=10**9):
    """Generate a random array for test cases."""
    length = random.randint(min_length, max_length)
    return [random.randint(0, max_value) for _ in range(length)]


def generate_test_cases(num_cases=50, max_length=500, max_value=10**9):
    """Generate test cases for the Partition Array for Maximum Sum problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        arr = generate_random_array(1, max_length, max_value)
        k = random.randint(1, len(arr))
        expected_output = solution.maxSumAfterPartitioning(arr, k)
        test_cases.append({
            "input": {
                "arr": arr,
                "k": k
            },
            "output": expected_output
        })

    # Add predefined edge cases
    predefined_cases = [
        {"input": {"arr": [1, 15, 7, 9, 2, 5, 10], "k": 3},
         "output": solution.maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3)},
        {"input": {"arr": [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], "k": 4},
         "output": solution.maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4)},
        {"input": {"arr": [1], "k": 1},
         "output": solution.maxSumAfterPartitioning([1], 1)},
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
    max_value = 10**9
    test_cases = generate_test_cases(num_cases, max_length, max_value)
    save_test_cases("../test_cases_1043.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'max_sum_partition_test_cases.json'.")
