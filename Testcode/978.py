import json
import random


class Solution:
    def maxTurbulenceSize(self, arr):
        n = len(arr)
        l, r = 0, 0
        ans = 1
        if n == 1:
            return 1
        while r < n:
            while l < n - 1 and arr[l] == arr[l + 1]:  # Handle duplicates
                l += 1
            while r < n - 1 and (arr[r - 1] > arr[r] < arr[r + 1] or arr[r - 1] < arr[r] > arr[r + 1]):
                r += 1
            ans = max(ans, r - l + 1)
            l = r
            r += 1
        return ans


def generate_random_array(max_length=40000, max_value=10**9):
    """Generate a random array of integers."""
    length = random.randint(1, max_length)
    return [random.randint(0, max_value) for _ in range(length)]


def generate_test_cases(num_cases=50, max_length=40000, max_value=10**9):
    """Generate test cases for the Maximum Turbulent Subarray problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        arr = generate_random_array(max_length, max_value)
        expected_output = solution.maxTurbulenceSize(arr)
        test_cases.append({"input": arr, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": [9, 4, 2, 10, 7, 8, 8, 1, 9], "output": solution.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9])},
        {"input": [4, 8, 12, 16], "output": solution.maxTurbulenceSize([4, 8, 12, 16])},
        {"input": [100], "output": solution.maxTurbulenceSize([100])},
        {"input": [100, 100, 100], "output": solution.maxTurbulenceSize([100, 100, 100])},
        {"input": [1, 2, 1, 2, 1, 2], "output": solution.maxTurbulenceSize([1, 2, 1, 2, 1, 2])},
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
    max_length = 40000
    max_value = 10**9
    test_cases = generate_test_cases(num_cases, max_length, max_value)
    save_test_cases("test_cases_978.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'max_turbulent_subarray_test_cases.json'.")
