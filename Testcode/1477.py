import json
import random
from typing import List
import collections


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        def get_sub_arrays(arr):
            lookup = collections.defaultdict(int)
            running_sum = 0
            dp = [float('inf')] * len(arr)

            for i, num in enumerate(arr):
                running_sum += num
                if running_sum == target:
                    dp[i] = i - 0 + 1
                elif running_sum - target in lookup:
                    dp[i] = i - lookup[running_sum - target] + 1
                lookup[running_sum] = i + 1
                dp[i] = min(dp[i - 1], dp[i])
            return dp

        dp_left = get_sub_arrays(arr)
        dp_right = get_sub_arrays(arr[::-1])[::-1]

        ans = float('inf')
        for i in range(1, len(arr)):
            ans = min(ans, dp_left[i - 1] + dp_right[i])
        return ans if ans != float('inf') else -1


# Helper function to generate random test cases
def generate_test_case():
    length = random.randint(1, 10 ** 5)
    arr = [random.randint(1, 1000) for _ in range(length)]
    target = random.randint(1, min(10 ** 8, sum(arr)))
    return arr, target


# Generate and save test cases
def generate_test_cases(num_cases=10):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        arr, target = generate_test_case()
        # Compute expected output using the provided solution
        expected_output = solution.minSumOfLengths(arr, target)
        test_cases.append({
            "input": {"arr": arr, "target": target},
            "output": expected_output
        })

    # Save to JSON file
    with open("test_cases_1477.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
