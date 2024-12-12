import json
import random
from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_sum_ending = [float('-inf')] * n
        prefix_sum_starting = [float('-inf')] * n
        prefix_sum_ending[n - 1] = arr[n - 1]
        prefix_sum_starting[0] = arr[0]

        for i in range(1, n):
            prefix_sum_starting[i] = max(prefix_sum_starting[i - 1] + arr[i], arr[i])
        for i in range(n - 2, -1, -1):
            prefix_sum_ending[i] = max(prefix_sum_ending[i + 1] + arr[i], arr[i])

        max_without_deletion = max(prefix_sum_starting)
        max_with_deletion = float('-inf')
        for i in range(1, n - 1):
            max_with_deletion = max(max_with_deletion, prefix_sum_starting[i - 1] + prefix_sum_ending[i + 1])

        return max(max_without_deletion, max_with_deletion)


def generate_random_array(min_length=1, max_length=10**5, min_value=-10**4, max_value=10**4):
    """Generate a random array of integers."""
    length = random.randint(min_length, max_length)
    return [random.randint(min_value, max_value) for _ in range(length)]


def generate_test_cases(num_cases=50, max_length=1000):
    """Generate test cases for the Maximum Sum with One Deletion problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        arr = generate_random_array(1, max_length)
        expected_output = solution.maximumSum(arr)
        test_cases.append({"input": arr, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": [1, -2, 0, 3], "output": solution.maximumSum([1, -2, 0, 3])},
        {"input": [1, -2, -2, 3], "output": solution.maximumSum([1, -2, -2, 3])},
        {"input": [-1, -1, -1, -1], "output": solution.maximumSum([-1, -1, -1, -1])},
        {"input": [5], "output": solution.maximumSum([5])},
        {"input": [10, -1, 10, -1, 10], "output": solution.maximumSum([10, -1, 10, -1, 10])},
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
    max_length = 1000
    test_cases = generate_test_cases(num_cases, max_length)
    save_test_cases("test_cases_1186.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'maximum_sum_with_one_deletion_test_cases.json'.")
