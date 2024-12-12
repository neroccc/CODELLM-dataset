import json
import random
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod, n = 10 ** 9 + 7, len(arr)
        odd_sum, even_sum, curr_sum, ans = 0, 1, 0, 0
        for i in arr:
            curr_sum += i
            if curr_sum % 2 == 1:
                odd_sum += 1
                ans += even_sum % mod
            else:
                even_sum += 1
                ans += odd_sum % mod
        ans %= mod
        return ans


# Helper function to generate random arrays
def generate_random_array(length):
    return [random.randint(1, 100) for _ in range(length)]


# Generate test cases
def generate_test_cases(num_cases=10):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        length = random.randint(1, 10 ** 5)
        arr = generate_random_array(length)

        # Compute expected output using the provided solution
        expected_output = solution.numOfSubarrays(arr)

        test_cases.append({
            "input": {"arr": arr},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1524.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
